#!/usr/bin/node
// Writes a string to a file.
const fs = require('fs');
// The first argument is the file path
const filePath = process.argv[2];
// The second argument is the string to write
const stringInput = process.argv[3];
// Writes the sting content to a file
fs.writeFile(filePath, stringInput, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
