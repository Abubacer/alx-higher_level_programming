#!/usr/bin/node
// A  script that prints two arguments passed to it, in the following format: “is".

const [, , firstArg, secondArg] = process.argv;
console.log(firstArg + ' is ' + secondArg);
