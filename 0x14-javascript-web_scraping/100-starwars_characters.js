#!/usr/bin/node
// Prints all characters of a Star Wars movie.
const request = require('request');
// The first argument is the Movie ID
const movieId = process.argv[2];
// Star wars API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
// Fetchs movie information
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movieData = JSON.parse(body);
    const characterUrl = movieData.characters;

    characterUrl.forEach((character) => {
      request(character, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
