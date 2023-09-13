#!/usr/bin/node
// A script that concats 2 files.
const fs = require('fs').promises;
const srcFile1 = process.argv[2];
const srcFile2 = process.argv[3];
const destFile = process.argv[4];

fs.readFile(srcFile1, 'utf8')
  .then(data1 => fs.writeFile(destFile, data1, 'utf8'))
  .catch(error => console.error(error));

fs.readFile(srcFile2, 'utf8')
  .then(data2 => fs.writeFile(destFile, data2, { flag: 'a' }, 'utf8'))
  .catch(error => console.error(error));
