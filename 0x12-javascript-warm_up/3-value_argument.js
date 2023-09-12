#!/usr/bin/node
const [, , firstArg] = process.argv;

// A script that prints the first argument passed to it.
if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
