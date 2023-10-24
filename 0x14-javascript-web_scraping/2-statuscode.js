#!/usr/bin/node
// Display the status code of a GET request.
const request = require('request');
// The first argument is the url to request
const urlPath = process.argv[2];
// The status code is printed like this: code: <status code>
request(urlPath, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
