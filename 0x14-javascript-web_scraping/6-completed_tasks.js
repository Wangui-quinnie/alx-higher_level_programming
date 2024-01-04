#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const todosData = JSON.parse(body);

    const completedTasksByUser = {};

    todosData.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
