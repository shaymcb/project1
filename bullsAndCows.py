#Shaylee McBride
#4Apr2018
#bullsAndCows.py - mastermind

from ggame import *
from random import randint

red = Color(0xFF0000,1)
orange = Color(0xFFA500,1)
yellow = Color(0xFFFF00,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
purple = Color(0xFF00FF,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

def pickCode():
    firstDigit = str(randint(0,9))
    otherDigits = str(randint(100,999))
    return firstDigit+otherDigits
