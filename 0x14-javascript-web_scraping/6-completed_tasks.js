#!/usr/bin/node
// Prints and computes the number of tasks completed by user id.
const request = require('request');
// The first argument is the API URL
const apiUrl = process.argv[2];
// Fetchs todos data by user
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todosData = JSON.parse(body);
    const completedTasks = {};

    todosData.forEach((task) => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
