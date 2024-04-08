#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square

        Args:
            size = size of the new square
            x = x coordinate of new square
            y = y coordinate of the new square
            id = identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """defines the setter of the square class"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """the update function assigns attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                """enumerates over each args"""
                setattr(self, attrs[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def to_dictionary(self):
        """ Dictionary representation of the Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
