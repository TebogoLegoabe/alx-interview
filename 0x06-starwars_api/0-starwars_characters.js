#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  return new Promise((resolve, reject) => {
    request(apiUrl, (err, _, body) => {
      if (err) {
        reject(err);
      }

      const charactersURL = JSON.parse(body).characters;
      const charactersName = charactersURL.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
      );

      Promise.all(charactersName)
        .then(names => resolve(names))
        .catch(allErr => reject(allErr));
    });
  });
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  getMovieCharacters(movieId)
    .then(names => console.log(names.join('\n')))
    .catch(err => console.error(err));
} else {
  console.error('Usage: ./script.js <Movie ID>');
}
