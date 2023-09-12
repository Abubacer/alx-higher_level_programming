#!/usr/bin/node
// A script that prints My number: <first argument converted in integer> if the first argument can be converted to an int.

const [, , firstArg] = process.argv;
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(firstArg));
}
