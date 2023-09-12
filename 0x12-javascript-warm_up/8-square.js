#!/usr/bin/node
// A script that prints a square.

const [, , firstArg] = process.argv;
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log('X'.repeat(parseInt(firstArg)));
  }
}
