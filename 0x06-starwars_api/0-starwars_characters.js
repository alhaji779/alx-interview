#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// URL for the Star Wars API
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch movie data and print character names
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body);

  // Get the list of character URLs
  const characterUrls = movieData.characters;

  // Fetch and print each character name
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      // Parse the character data and print the name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
