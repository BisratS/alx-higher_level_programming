#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    // Convert JSON TO Objects
    const todos = JSON.parse(body);
    // Create dictionary
    const TaskCompleted = {};
    for (let i = 0; i < todos.length; i++) {
      // verify task completed
      if (todos[i].completed === true) {
        if (TaskCompleted[todos[i].userId] === undefined) {
          TaskCompleted[todos[i].userId] = 0;
        }
        TaskCompleted[todos[i].userId]++;
      }
    }
    // print task completed dictionary
    console.log(TaskCompleted);
  }
});
