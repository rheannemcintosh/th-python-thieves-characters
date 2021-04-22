# ---------------------------------------------------------------- #
#
# thieves.py
#
# This is a simple object oriented Python program to create 
# thieves and their attributes. Built in conjuntion with 
# the Object Oriented Python course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Import statements
import random
from attributes import Agile, Sneaky
from characters import Character


# Create a Thief class
class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
