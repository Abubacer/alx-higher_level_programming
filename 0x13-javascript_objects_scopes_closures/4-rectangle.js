#!/usr/bin/node
// A class Rectangle that defines a rectangle.
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  // Prints the rectangle using the character X.
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Exchanges the width and the height of the rectangle.
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  // Multiples the width and the height of the rectangle by 2.
  double () {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
};
