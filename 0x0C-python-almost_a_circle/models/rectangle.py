#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle.

        Args:
            id (int): the id of the Rectangle.
            width (int): the Rectangle width.
            height (int): the Rectangle height.
            x (int): the x position of the Rectangle.
            y (int): the y position of the Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter and setter for the Rectangle width attribute.

        Raises:
            TypeError: If the width is not an int.
            ValueError: If the width is less than or equal to Zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter for the Rectangle height attribute.

        Raises:
            TypeError: If the height is not an int.
            ValueError: If the height is less than or equal to Zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter and setter for the Rectangle x attribute.

        Raises:
            TypeError: If the x is not an int.
            ValueError: If the x is less than Zero.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter and setter for the Rectangle y attribute.

        Raises:
            TypeError: If the y is not an int.
            ValueError: If the y is less than Zero.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for n in range(self.__y):
            print("")
        for n in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """Returns a string string representation of the rectangle."""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.

        Args:
            args: the positional args, skipped if not empty.
                the first arg assigns to the id.
                the seconde arg assigns to the width.
                the third arg assigns to the height.
                the fourth arg assigns to the x.
                the fifth arg assigns to the y.
            kwargs: The keyword args representing the key/value to assign
                to the attributes.
        """
        if args:
            if len(args) > 5:
                raise ValueError("Too many positional args provided")
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
