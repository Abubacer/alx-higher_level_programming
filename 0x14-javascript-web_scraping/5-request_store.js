#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');
// The first argument is the URL to request
const webPageUrl = process.argv[2];
// The second argument is the file path to store the body response
const filePath = process.argv[3];

request(webPageUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
