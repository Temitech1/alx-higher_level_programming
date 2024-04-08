#!/usr/bin/python3
"""represents a rectangle using geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): the width of the new Rectangle.
            height (int): the height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
