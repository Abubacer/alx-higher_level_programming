#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given int.
const request = require('request');
// The first argument is the movie ID
const movieId = process.argv[2];
// The Star wars API url
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
// Fetchs movie information
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
