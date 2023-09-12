#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.

const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  const argsList = argv.sort();
  console.log(argsList.reverse()[1]);
}
