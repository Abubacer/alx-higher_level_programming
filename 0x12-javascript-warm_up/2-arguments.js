#!/usr/bin/node
const argv = require('process').argv;

// A script that prints a message depending of the number of arguments passed.
if (argv.length <= 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
