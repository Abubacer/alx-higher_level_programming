#!/usr/bin/node
// A function that prints the number of arguments already printed and the new argument value.
let argCount = 0;
exports.logMe = function (item) {
  console.log(`${argCount++}: ${item}`);
};
