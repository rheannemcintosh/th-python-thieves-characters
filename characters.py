# ---------------------------------------------------------------- #
#
# characters.py
#
# This is a simple object oriented Python program to create 
# thieves and their attributes. Built in conjuntion with 
# the Object Oriented Python course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Create the Character class
class Character:

    def __init__(self, name="", **kwargs):
        if not name:
            raise ValueError("'name' is required!")

        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)
