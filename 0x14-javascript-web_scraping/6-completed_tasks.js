#!/usr/bin/node
/*
computes the number of tasks completed by user id
*/
const axios = require('axios');
const dictUser = {};

axios({
  method: 'GET',
  url: process.argv[2]
})
  .then(response => {
    response.data.forEach(task => {
      if (task.completed === true) {
        if (dictUser[task.userId] === undefined) {
          dictUser[task.userId] = 0;
        }
        dictUser[task.userId] += 1;
      }
    });
    console.log(dictUser);
  })
  .catch(err => console.log(err));
