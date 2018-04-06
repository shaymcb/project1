#Shaylee McBride
#4Apr2018
#bullsAndCows.py - mastermind

from ggame import *
from random import randint

#colors
red = Color(0xFF0000,1)
orange = Color(0xFFA500,1)
yellow = Color(0xFFFF00,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
violet = 
pink = Color(0xFF00FF,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
outline = LineStyle(2,black)

def pickCode():
    firstDigit = str(randint(0,9))
    otherDigits = str(randint(100,999))
    return firstDigit+otherDigits

def turnColor(color):
    Circle = CircleAsset(20,outline,color)
    if data['guesses'] <= 40:
        Sprite(Circle,((data['guesses'] - data['guesses']//4 * 4)*45, data['guesses']//4 * 45))
        data['guesses'] += 1

def turnRed(event):
    turnColor(red)
    data['guess'] += '1'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnOrange(event):
    turnColor(orange)
    data['guess'] += '2'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnYellow(event):
    turnColor(yellow)
    data['guess'] += '3'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnGreen(event):
    turnColor(green)
    data['guess'] += '4'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnBlue(event):
    turnColor(blue)
    data['guess'] += '5'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnPink(event):
    turnColor(pink)
    data['guess'] + '6'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])


def checkAnswer(answer):
    print(data['guess'])
    data['guess'] = ''
    

if __name__ == '__main__':
    data = {}
    data['guesses'] = 0
    data['guess'] = ""
    
    emptyCircle = CircleAsset(20,outline,white)
    
    #guessing grid
    circlex = 0
    circley = 0
    for i in range(10):
        for j in range(4):
            Sprite(emptyCircle,(circlex + j*45,circley + i*45))
    
    App().listenKeyEvent('keydown','r',turnRed)
    App().listenKeyEvent('keydown','o',turnOrange)
    App().listenKeyEvent('keydown','y',turnYellow)
    App().listenKeyEvent('keydown','g',turnGreen)
    App().listenKeyEvent('keydown','b',turnBlue)
    App().listenKeyEvent('keydown','p',turnPink)
    App().listenKeyEvent('keydown','v',turnViolet)
    App().listenKeyEvent('keydown','w',turnWhite)
    
    
    App().run()
    
    
    
