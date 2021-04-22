# ---------------------------------------------------------------- #
#
# play.py
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
from thieves import Thief

# Play the game - default code to test the program works
rheanne = Thief(name="Rheanne", sneaky=False)
print(rheanne.sneaky)
print(rheanne.agile)
print(rheanne.hide(8))
