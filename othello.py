#Shaylee McBride
#23May2018
#othello.py

from ggame import *

BOX_SIZE = 70

#set board and starting position
def buildBoard():
    for rows in range(8):
        L = []
        for cols in range(8):
            Sprite(box,(cols*BOX_SIZE,rows*BOX_SIZE))
            L.append('')
        pieceList.append(L)
     
    spriteList.append(Sprite(blackCircle,(3*BOX_SIZE,4*BOX_SIZE)))
    spriteList.append(Sprite(blackCircle,(4*BOX_SIZE,3*BOX_SIZE)))    
    spriteList.append(Sprite(whiteCircle,(4*BOX_SIZE,4*BOX_SIZE)))
    spriteList.append(Sprite(whiteCircle,(3*BOX_SIZE,3*BOX_SIZE)))
    
    pieceList[4][3] = 'b'
    pieceList[3][4] = 'b'
    pieceList[4][4] = 'w'
    pieceList[3][3] = 'w'
    
def mouseClick(event):
    clickCol = event.x//BOX_SIZE
    clickRow = event.y//BOX_SIZE
    color = 'b'
    
    sameRow = False
    sameCol = False
    sameDiag = False
    if 


if __name__ == '__main__':
    pieceList = []
    spriteList = []
    green = Color(0x00FF00, 1)
    white = Color(0xFFFFFF, 1)
    black = Color(0x000000, 1)
    outline = LineStyle(1,black)
    
    box = RectangleAsset(BOX_SIZE,BOX_SIZE,outline,green)
    blackCircle  = CircleAsset(BOX_SIZE/2,outline,black)
    whiteCircle = CircleAsset(BOX_SIZE/2,outline,white)
    
    buildBoard()
    
    App.listenMouseEvent('click',mouseClick)
    
    App().run()
