#!/usr/bin/node
/* eslint-disable no-console */
const axios = require('axios');

const movieId = Number(process.argv[2]);

async function getCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}

(async function fetchAndPrintCharacters() {
  try {
    const response = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characterUrls = Array.from(response.data.characters);

    // Use `Promise.all` to resolve all Promises concurrently
    const characterNames = await Promise.all(
      characterUrls.map((link) => getCharacterName(link)),
    );

    // Print character names
    characterNames.forEach((character) => {
      console.log(character);
    });
  } catch (error) {
    console.error('Error:', error);
  }
}());
