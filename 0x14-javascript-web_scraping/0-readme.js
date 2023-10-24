#!/usr/bin/node
// Reads and prints the content of a file in utf-8.
const fs = require('fs');
// The first argument is the file path
const filePath = process.argv[2];
// Reads and prints the content of a file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
