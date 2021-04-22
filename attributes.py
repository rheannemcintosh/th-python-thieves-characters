# ---------------------------------------------------------------- #
#
# attributes.py
#
# This is a simple object oriented Python program to create 
# thieves and their attributes. Built in conjuntion with 
# the Object Oriented Python course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Import random
import random


# Create a Sneaky sttribute class
class Sneaky:
    sneaky = True

    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sneaky = sneaky

    def hide(self, light_level):
        return self.sneaky and light_level < 10

# Create an Agile attribute class
class Agile:
    agile = True

    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agile = agile

    def evade(self):
        return self.agile and random.randint(0, 1)
