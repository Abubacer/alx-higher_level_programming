#!/usr/bin/node
// A script that prints the addition of 2 integers.

const [, , firstArg, secondArg] = process.argv;
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(firstArg, secondArg));
