#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
// The first argument is the API URL
const apiUrl = process.argv[2];
// Fetchs movie information
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movieData = JSON.parse(body).results;
    const characterId = '18';
    const numberOfMovies = movieData.filter((movie) =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(numberOfMovies.length);
  }
});
