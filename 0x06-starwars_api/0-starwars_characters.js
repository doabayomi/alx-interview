#!/usr/bin/node
/* eslint-disable no-console */
const util = require('util');
const request = util.promisify(require('request'));

const movieId = Number(process.argv[2]);

function getCharacterName(characterUrl, callback) {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      callback(null);
    } else {
      const data = JSON.parse(body);
      callback(data.name);
    }
  });
}

function fetchAndPrintCharacters() {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const data = JSON.parse(body);
    const characterUrls = Array.from(data.characters);

    let completedRequests = 0;
    const characterNames = [];

    characterUrls.forEach((link, index) => {
      getCharacterName(link, (name) => {
        if (name) {
          characterNames[index] = name;
        }
        // eslint-disable-next-line no-plusplus
        completedRequests++;

        if (completedRequests === characterUrls.length) {
          // Print character names in the order of the original requests
          characterNames.forEach((character) => {
            console.log(character);
          });
        }
      });
    });
  });
}

fetchAndPrintCharacters();
