#!/usr/bin/node
// Reads and prints the content of a file in utf-8.
const fs = require('fs');
// The first argument is the file path
const filePath = process.argv[2];
// The second argument is the string to write
const stringInput = process.argv[3];
// Reads and prints the content of a file
fs.writeFile(filePath, stringInput, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
