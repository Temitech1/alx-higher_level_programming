#!/usr/bin/python3
"""Defines a class square that inherits from Rectangle."""
Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """represents a Square"""

    def __init__(self, size):
        """initializes the square.
        Args:
            size(int) value of a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
