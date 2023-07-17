#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square.

        Args:
            id (int): the id of the Square.
            size (int): the square size.
            x (int): the x position of the Square.
            y (int): the y position of the Square.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter and setter for the Square size attribute.

        Raises:
            TypeError: If the size is not an int.
            ValueError: If the size is less than or equal to Zero.
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
      

    def __str__(self):
        """Returns a string string representation of the rectangle."""
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}"
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.

        Args:
            args: the positional args, skipped if not empty.
                the first arg assigns to the id.
                the seconde arg assigns to the size.
                the third arg assigns to the x.
                the fourth arg assigns to the y.
            kwargs: The keyword args representing the key/value to assign
                to the attributes.
        """
        if args:
            if len(args) > 4:
                raise ValueError("Too many positional args provided")
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
