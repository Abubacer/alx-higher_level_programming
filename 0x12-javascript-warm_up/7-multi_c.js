#!/usr/bin/node
// A script that prints x times “C is fun”.

const [, , firstArg] = process.argv;
if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log('C is fun');
  }
}
