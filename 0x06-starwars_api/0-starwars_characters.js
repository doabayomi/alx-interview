#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));

const API_URL = 'https://swapi-api.hbtn.io/api';

async function starwarsCharacters() {
  const endpoint = `${API_URL}/films/${process.argv[2]}/`;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const {characters} = response;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters();
