#Shaylee McBride
#4Apr2018
#bullsAndCows.py - mastermind

from ggame import *
from random import randint

RADIUS = 20
ATTEMPTS = 10


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
    pick1 = randint(0,9)
    pick2 = randint(0,9)
    pick3 = randint(0,9)
    pick4 = randint(0,9)
    
    while pick2 == pick1:
        pick2 = randint(0,9)
    while pick3 == pick1 or pick3 == pick2:
        pick3 = randint(0,9)
    while pick4 == pick1 or pick4 == pick2 or pick4 == pick3:
        pick4 = randint(0,9)
    
    data['code1'] = str(pick1)
    data['code2'] = str(pick2)
    data['code3'] = str(pick3)
    data['code4'] = str(pick4)
    
    return data['code1'] + data['code2'] + data['code3'] + data['code4']

def turnColor(color):
    Circle = CircleAsset(20,outline,color)
    if data['guesses'] <= 4 * ATTEMPTS:
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
    if checkBulls(data['guess']) == 4:
        print("YOU WIN!")
    else:
        print('bulls:',checkBulls(data['guess']))
        print('cows:',checkCows(data['guess']))
    data['guess'] = ''

def checkBulls(answer):
    bulls = 0
    i = 0
    for ch in data['guess']:
        i += 1
        if i == 1:
            if ch == data['code1']:
                bulls += 1
        elif i == 2:
            if ch == data['code2']:
                bulls+=1
        elif i == 3:
            if ch == data['code3']:
                bulls+=1
        else:
            if ch == data['code4']:
                bulls+=1
    return bulls
    
def checkCows(answer):
    cows = 0
    match = ''
    for ch in data['guess']:
        if ch in data['code'] and ch not in match:
            cows += 1
            match = match + ch
    return cows - checkBulls(data['guess'])
    

if __name__ == '__main__':
    data = {}
    data['code1'] = ''
    data['code2'] = ''
    data['code3'] = ''
    data['code4'] = ''
    data['code'] = pickCode()
    data['guesses'] = 0
    data['guess'] = ""
    
    print(data['code'])
    emptyCircle = CircleAsset(RADIUS,outline,grey)
    key = TextAsset('Colors = r, o, y, g, c, b, p, v, w, d')
    
    #guessing grid
    circlex = 0
    circley = 0
    for i in range(ATTEMPTS):
        for j in range(4):
            Sprite(emptyCircle,(circlex + j*(2*RADIUS+5),circley + i*(2*RADIUS+5)))
    
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
    
    
    
