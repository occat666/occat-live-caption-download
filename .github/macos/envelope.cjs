// Hybrid encryption for private build diagnostics. Only the public key is deployed.
const crypto = require('node:crypto');
const fs = require('node:fs');
const {pipeline} = require('node:stream/promises');

async function main() {
  const [mode, keyPath, input, output] = process.argv.slice(2);
  if (mode === 'generate') {
    const pair = crypto.generateKeyPairSync('rsa', {modulusLength: 3072,
      publicKeyEncoding: {type:'spki', format:'pem'},
      privateKeyEncoding: {type:'pkcs8', format:'pem'}});
    fs.writeFileSync(keyPath, pair.privateKey, {mode:0o600, flag:'wx'});
    fs.writeFileSync(input, pair.publicKey, {flag:'wx'});
    return;
  }
  if (mode === 'encrypt') {
    const key = crypto.randomBytes(32), nonce = crypto.randomBytes(12);
    const wrapped = crypto.publicEncrypt({key:fs.readFileSync(keyPath),
      oaepHash:'sha256', padding:crypto.constants.RSA_PKCS1_OAEP_PADDING}, key);
    const header = Buffer.alloc(6);
    header.write('OCCA', 0); header.writeUInt16BE(wrapped.length,4);
    const prefix = Buffer.concat([header, wrapped, nonce]);
    fs.writeFileSync(output, prefix, {flag:'wx'});
    const cipher = crypto.createCipheriv('aes-256-gcm',key,nonce);
    cipher.setAAD(prefix);
    await pipeline(fs.createReadStream(input), cipher, fs.createWriteStream(output,{flags:'a'}));
    fs.appendFileSync(output,cipher.getAuthTag());
    return;
  }
  if (mode === 'decrypt') {
    const fd = fs.openSync(input,'r'), header = Buffer.alloc(6);
    fs.readSync(fd,header,0,6,0);
    if (header.subarray(0,4).toString() !== 'OCCA') throw Error('Invalid envelope');
    const length=header.readUInt16BE(4), prefix=Buffer.alloc(6+length+12);
    fs.readSync(fd,prefix,0,prefix.length,0);
    const total=fs.fstatSync(fd).size, tag=Buffer.alloc(16);
    fs.readSync(fd,tag,0,16,total-16); fs.closeSync(fd);
    const key=crypto.privateDecrypt({key:fs.readFileSync(keyPath),oaepHash:'sha256',
      padding:crypto.constants.RSA_PKCS1_OAEP_PADDING},prefix.subarray(6,6+length));
    const decipher=crypto.createDecipheriv('aes-256-gcm',key,prefix.subarray(6+length));
    decipher.setAAD(prefix); decipher.setAuthTag(tag);
    try {
      await pipeline(fs.createReadStream(input,{start:prefix.length,end:total-17}),
        decipher,fs.createWriteStream(output,{flags:'wx',mode:0o600}));
    } catch(e) { fs.rmSync(output,{force:true}); throw e; }
    return;
  }
  throw Error('Unknown operation');
}
main().catch(()=>{process.stderr.write('Diagnostic envelope operation failed\n');process.exitCode=1;});
