#Shaylee McBride
#23May2018
#snek!

from ggame import *

from ggame import *
from random import randint

#constants
ROWS = 26  #all caps for constants
COLS = 50
CELL_SIZE = 20

#moves monkey right one cell if possible
def moveRight(event):
    for baby in snek:
        if baby.x < ((COLS-1)*CELL_SIZE):
            baby.x += CELL_SIZE
        if snek[0].x == fridge.x and snek[0].y == fridge.y:
            moveFridge()
            updateScore()
            
#moves monkey left one cell if possible
def moveLeft(event):
    for baby in snek:
        if baby.x > 0:
            baby.x -= CELL_SIZE
        if snek[0].x == fridge.x and snek[0].y == fridge.y:
            moveFridge()
            updateScore()
            
#moves monkey up one cell if possible        
def moveUp(event):
    for baby in snek:
        if baby.y > 0:
            baby.y -= CELL_SIZE
        if snek[0].x == fridge.x and snek[0].y == fridge.y:
            moveFridge()
            updateScore()
            
#moves monkey down one cell if possible
def moveDown(event):
    for baby in snek:
        if snek[0].y < ((ROWS-1)*CELL_SIZE):
            baby.y += CELL_SIZE
        if snek[0].x == fridge.x and snek[0].y == fridge.y:
            moveFridge()
            updateScore()

#moves banana to random location and resets timer
def moveFridge():
    data['frames'] = 0
    fridge.x = randint(0,COLS-1)*CELL_SIZE
    fridge.y = randint(0,ROWS-1)*CELL_SIZE

#increases score and displays new text at bottom of screen
def updateScore():
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))

#keeps track of how many frames have happened and moves banana if if 
#has been more than a random number between 50 and 300 (exciting!!)
def step():
    data['frames'] += 1
    if data['frames'] == randint(50,200):
        moveFridge()
        snek.append(Sprite(data['snekBox']),(randint(0,COLS*CELL_SIZE),randint(0,ROWS*CELL_SIZE)))

#sets up and runs the game
if __name__ == '__main__':
    
    #hold variables in dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    data['snekLength'] = 1
    
    #colors
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    yellow = Color(0xFFFF00,1)
    
    #graphics
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(2,black),black)
    data['snekBox'] = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(2,yellow),yellow)
    fridgeBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(2,white),white)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    snek = [Sprite(data['snekBox'])]
    fridge = Sprite(fridgeBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(step)
