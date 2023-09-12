#!/usr/bin/node
// A class Square that defines a square and inherits from Square of 5-square.js.
module.exports = class Square extends require('./5-square.js') {
  // Prints the rectangle using the character c.
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
