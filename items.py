# ---------------------------------------------------------------- #
#
# items.py
#
# This is a simple object oriented Python program to create 
# thieves and their attributes. Built in conjuntion with 
# the Object Oriented Python course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Create the Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)


# Create the Weapon class
class Weapon(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power
