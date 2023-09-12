#!/usr/bin/node
// A function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let elmnt = 0; elmnt < list.length; elmnt++) {
    if (list[elmnt] === searchElement) {
      count++;
    }
  }

  return count;
};
