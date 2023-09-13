#!/usr/bin/node
// A function that returns the reversed version of a list.
exports.esrever = function (list) {
  const reverseIt = [];
  for (let elmnt = list.length - 1; elmnt >= 0; elmnt--) {
    reverseIt.push(list[elmnt]);
  }

  return reverseIt;
};
