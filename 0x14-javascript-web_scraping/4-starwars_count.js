#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body);

    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('18')) {
          count++;
          break;
        }
      }
    }

    console.log(count);
  } else {
    console.log(error);
  }
});
