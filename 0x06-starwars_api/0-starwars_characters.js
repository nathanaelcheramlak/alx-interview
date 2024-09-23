#!/usr/bin/node

const request = require("request");
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch each character's name in order using a loop
  printCharacters(characters, 0);
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return; // End of the list, stop recursion
  }

  request(characters[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
      return;
    }

    const characterData = JSON.parse(charBody);
    console.log(characterData.name);

    // Call the function recursively for the next character
    printCharacters(characters, index + 1);
  });
}
