#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle.
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
