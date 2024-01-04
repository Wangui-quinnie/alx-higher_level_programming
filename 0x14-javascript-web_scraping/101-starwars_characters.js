#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    const printCharacter = (index) => {
      if (index < charactersUrls.length) {
        const characterUrl = charactersUrls[index];
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            printCharacter(index + 1);
          }
        });
      }
    };
    printCharacter(0);
  }
});
