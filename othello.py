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
    clickCol = int(event.x//BOX_SIZE)
    clickRow = int(event.y//BOX_SIZE)
    color = 'b'
    othercolor = 'w'
    sameRow = False
    sameCol = False
    sameDiag1 = False
    sameDiag2 = False
    
    for i in range(-1*min(1,clickRow),min(1,7-clickRow)):
        for j in range(-1*min(1,clickCol),min(1,7-clickCol)):
            if pieceList[clickRow+i][clickCol+j] == 'w':

    
    if color in pieceList[clickRow]:
        sameRow = True
    
    for row in pieceList:
        if row[clickCol] == color:
            sameCol = True
            break

    for i in range(-1*(min(clickCol,clickRow)),min(8-clickCol,8-clickRow)):
        if pieceList[clickRow+i][clickCol+i] == color:
            sameDiag1 = True
            break
    
    for i in range(-1*(min(clickCol,7-clickRow)),min(8-clickCol,clickRow)):
        if pieceList[clickRow-i][clickCol+i] == color:
            sameDiag2 = True
            break
        
    print(sameRow,sameCol,sameDiag1,sameDiag2)

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
