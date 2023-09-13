#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const { dict } = require('./101-data');
const userIds = {};
for (const k in dict) {
  const occurrence = dict[k];
  if (!userIds[occurrence]) {
    userIds[occurrence] = [];
  }
  userIds[occurrence].push(k);
}

console.log(userIds);
