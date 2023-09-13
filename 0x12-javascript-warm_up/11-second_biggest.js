#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.
const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  const argsToNumb = argv.slice(2).map(Number);
  const sortedList = argsToNumb.sort((x, y) => y - x);
  console.log(sortedList[1]);
}
