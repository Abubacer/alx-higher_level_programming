#!/usr/bin/node
// Prints all characters of a Star Wars movie, in the same order of the list “characters” in the /films/ response.
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
    // Fetchs and prints character names
    const fetchCharacterName = (idx) => {
      if (idx < characterUrl.length) {
        request(characterUrl[idx], (err, res, body) => {
          if (err) {
            console.error(err);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            fetchCharacterName(idx + 1);// get the next character name
          }
        });
      }
    };
    // Start fetching data from the first character URL
    fetchCharacterName(0);
  }
});
