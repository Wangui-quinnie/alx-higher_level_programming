#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error('Error writing to file:', writeError);
      } else {
        console.log(`Content successfully written to ${filePath}.`);
      }
    });
  }
});
