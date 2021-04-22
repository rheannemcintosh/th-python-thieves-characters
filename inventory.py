# ---------------------------------------------------------------- #
#
# inventory.py
#
# This is a simple object oriented Python program to create 
# thieves and their attributes. Built in conjuntion with 
# the Object Oriented Python course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Create the Inventory class
class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        yield from self.slots
