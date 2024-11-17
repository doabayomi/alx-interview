#!/usr/bin/node
/* eslint-disable no-console */
// const fetch = require('node-fetch');

const movieId = Number(process.argv[2]);

async function getCharacterName(characterUrl) {
  try {
    const response = await fetch(characterUrl);
    const data = await response.json();
    return data.name;
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}

(async function fetchAndPrintCharacters() {
  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const response = await fetch(url);
    const data = await response.json();
    const characterUrls = Array.from(data.characters);

    const characterNames = await Promise.all(
      characterUrls.map((link) => getCharacterName(link)),
    );

    characterNames.forEach((character) => {
      console.log(character);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}());
