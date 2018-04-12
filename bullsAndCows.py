#Shaylee McBride
#4Apr2018
#bullsAndCows.py - mastermind

from ggame import *
from random import randint

#constants
RADIUS = 20   #how big the circles are
ATTEMPTS = 10 #how many tries you get

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

#returns the code to be guessed
def pickCode():
    #generates 4 random digits
    pick1 = randint(0,9)
    pick2 = randint(0,9)
    pick3 = randint(0,9)
    pick4 = randint(0,9)
    
    #if any of the four overlap, pick again until they don't
    while pick2 == pick1:
        pick2 = randint(0,9)
    while pick3 == pick1 or pick3 == pick2:
        pick3 = randint(0,9)
    while pick4 == pick1 or pick4 == pick2 or pick4 == pick3:
        pick4 = randint(0,9)
    
    #store it as a string because it's easier to work with
    data['code1'] = str(pick1)
    data['code2'] = str(pick2)
    data['code3'] = str(pick3)
    data['code4'] = str(pick4)
    
    return data['code1'] + data['code2'] + data['code3'] + data['code4']

#sprites a circle of the guessed color in the correct spot
def turnColor(color):
    Circle = CircleAsset(20,outline,color)
    if data['guesses'] < 4 * ATTEMPTS: #only goes for number of attempts possible
        Sprite(Circle,((data['guesses'] - data['guesses']//4 * 4)*45, data['guesses']//4 * 45))
        data['guesses'] += 1

#all of these do the same thing but with different colors:
#sets the color for turnColor() and checks answer if 4 have been guessed
def turnRed(event):
    if '0' not in data['guess']: #can't guess same color twice
        turnColor(red)
        data['guess'] += '0'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnOrange(event):
    if '1' not in data['guess']:
        turnColor(orange)
        data['guess'] += '1'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnYellow(event):
    if '2' not in data['guess']:
        turnColor(yellow)
        data['guess'] += '2'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnGreen(event):    
    if '3' not in data['guess']:
        turnColor(green)
        data['guess'] += '3'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnCyan(event):    
    if '4' not in data['guess']:
        turnColor(cyan)
        data['guess'] += '4'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnBlue(event):    
    if '5' not in data['guess']:
        turnColor(blue)
        data['guess'] += '5'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnPink(event):
    if '6' not in data['guess']:
        turnColor(pink)
        data['guess'] += '6'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnViolet(event):    
    if '7' not in data['guess']:
        turnColor(violet)
        data['guess'] += '7'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnWhite(event):    
    if '8' not in data['guess']:
        turnColor(white)
        data['guess'] += '8'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])
def turnDark(event):    
    if '9' not in data['guess']:
        turnColor(black)
        data['guess'] += '9'
        if data['guesses']%4 == 0:
                checkAnswer(data['guess'])

#checks 4-digit guess against answer code, displays bulls and cows
def checkAnswer(answer):
    if checkBulls(data['guess']) == 4: #if you got it right, displays win message in correct spot
        Sprite(winBox,(RADIUS*8 + 25, (data['guesses']/4-1)*(RADIUS*2+5)))
    elif data['guesses'] == ATTEMPTS * 4: #if you're out of guesses, displays lose message in correct spot
        Sprite(loseBox, (RADIUS*8 + 25, (ATTEMPTS-1)*(RADIUS*2+5)))
    else:
        bulls = checkBulls(data['guess'])
        cows = checkCows(data['guess'])
        scoreBox = TextAsset('Bulls = '+str(bulls)+' , Cows = '+str(cows))
        Sprite(scoreBox,(RADIUS*8 + 25, (data['guesses']/4-1)*(RADIUS*2+5)))
    
    data['guess'] = '' #reset guess and try again

#checks how many guessed colors are in right spot
#for each digit in the guess, checks against corresponding digit in code
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

#checks how many guessed colors are right, but in wrong spot
#counts colors in both guess and code and subtracts ones in right spot
def checkCows(answer):
    cows = 0
    match = '' 
    for ch in data['guess']:
        if ch in data['code']:
            cows += 1
    return cows - checkBulls(data['guess'])
    
if __name__ == '__main__':
    data = {}
    data['code1'] = ''
    data['code2'] = ''
    data['code3'] = ''
    data['code4'] = ''
    data['code'] = pickCode()
    data['guesses'] = 0  #total number of guessed colors
    data['guess'] = ""   #guessed code
    
    emptyCircle = CircleAsset(RADIUS,outline,grey)
    key = TextAsset('Possible Colors: r, o, y, g, c, b, p, v, w, d',width = 500)
    scoreBox = TextAsset('Bulls = 0, Cows = 0')
    winBox = TextAsset('YOU WIN!!!',style = 'bold 40pt Times')
    loseBox = TextAsset('YOU LOSE :(',style = 'bold 40pt Times',width = 200)

    #guessing grid
    circlex = 0
    circley = 0
    for i in range(ATTEMPTS):
        for j in range(4):
            Sprite(emptyCircle,(circlex + j*(2*RADIUS+5),circley + i*(2*RADIUS+5)))
    
    Sprite(key,(300,0))
    
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
    
    
    
