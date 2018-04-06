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
cyan = Color(0x00FFFF,1)
blue = Color(0x0000FF,1)
violet = Color(0x800080,1)
pink = Color(0xFF00FF,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
grey = Color(0xF2F2F2,1)
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
    data['guess'] += '0'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnOrange(event):
    turnColor(orange)
    data['guess'] += '1'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnYellow(event):
    turnColor(yellow)
    data['guess'] += '2'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnGreen(event):
    turnColor(green)
    data['guess'] += '3'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnCyan(event):
    turnColor(cyan)
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
    data['guess'] += '6'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnViolet(event):
    turnColor(violet)
    data['guess'] += '7'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnWhite(event):
    turnColor(white)
    data['guess'] += '8'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])
def turnDark(event):
    turnColor(black)
    data['guess'] += '9'
    if data['guesses']%4 == 0:
            checkAnswer(data['guess'])

def checkAnswer(answer):
    print(data['guess'])
    print('bulls:',checkBulls(data['guess']))
    print('cows:',checkCows(data['guess']))
    data['guess'] = ''

def checkBulls(answer):
    bulls = 0
    for i in range(4):
        if data['code'][i] == data['guess'][i]:
            bulls += 1
    return bulls
    
def checkCows(answer):
    cows = 0
    for ch in data['guess']:
        if ch in data['code']:
            cows += 1
    return cows - checkBulls(data['guess'])
    

if __name__ == '__main__':
    data = {}
    data['code'] = pickCode()
    data['guesses'] = 0
    data['guess'] = ""
    
    print(data['code'])
    emptyCircle = CircleAsset(20,outline,grey)
    
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
    App().listenKeyEvent('keydown','c',turnCyan)
    App().listenKeyEvent('keydown','b',turnBlue)
    App().listenKeyEvent('keydown','p',turnPink)
    App().listenKeyEvent('keydown','v',turnViolet)
    App().listenKeyEvent('keydown','w',turnWhite)
    App().listenKeyEvent('keydown','d',turnDark)
    
    App().run()
    
    
    
