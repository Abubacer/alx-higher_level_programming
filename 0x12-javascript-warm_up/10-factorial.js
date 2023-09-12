#!/usr/bin/node
// A script that computes and prints a factorial.

const [, , firstArg] = process.argv;
function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(firstArg));
