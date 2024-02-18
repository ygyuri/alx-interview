#!/usr/bin/node
const axios = require('axios');

const endpoint = 'https://swapi-api.hbtn.io/api';
const filmId = process.argv[2];

axios.get(`${endpoint}/films/${filmId}/`)
  .then(response => {
    const characters = response.data.characters;

    characters.forEach(async characterUrl => {
      try {
        const characterResponse = await axios.get(characterUrl);
        console.log(characterResponse.data.name);
      } catch (error) {
        console.error('Error:', error.message);
      }
    });
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
