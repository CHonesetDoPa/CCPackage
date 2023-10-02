const fs = require('fs');
const crypto = require('crypto');
const path = require('path');

const inputFile = 'encrypted.exe';
const outputFile = 'restored.txt';
const password = 'yourPassword';

const decipher = crypto.createDecipher('aes-256-cbc', password);

const input = fs.createReadStream(inputFile);
const output = fs.createWriteStream(outputFile);

input.pipe(decipher)
     .pipe(output);

output.on('finish', () => {
    console.log('File restored successfully.');
});
