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
    
    pieceList[4][3] = 1
    pieceList[3][4] = 1
    pieceList[4][4] = 2
    pieceList[3][3] = 2
    
def mouseClick(event):
    clickCol = int(event.x//BOX_SIZE)
    clickRow = int(event.y//BOX_SIZE)
    placed = False
    
    for i in range(-1*min(1,clickRow),min(2,8-clickRow)):
        for j in range(-1*min(1,clickCol),min(2,8-clickCol)):
            if pieceList[clickRow+i][clickCol+j] == data['otherPlayer'] and pieceList[clickRow][clickCol] == '':
                placed = True
                if data['player'] == 1:
                    spriteList.append(Sprite(blackCircle,(clickCol*BOX_SIZE,clickRow*BOX_SIZE)))
                else:
                    spriteList.append(Sprite(whiteCircle,(clickCol*BOX_SIZE,clickRow*BOX_SIZE)))
    
    if placed == True:
        flipWest(clickRow,clickCol)
        flipEast(clickRow,clickCol)
        
        data['player'] = 3 - data['player']
        data['otherPlayer'] = 3 - data['otherPlayer']
  
#works
def flipWest(row,col):
    if data['player'] in pieceList[row][:col]:
        pos = pieceList[row][:col].index(data['player'])
        for i in range(pos,col):
            if pieceList[row][i] == data['otherPlayer']:
                pieceList[row][i] = data['player']
                print(True)

def flipEast(row,col):
    if data['player'] in pieceList[row][col:]:
        pos = pieceList[row][col:].index(data['player'])
        print(pos) #this is wrong idk why
        for i in range(col,pos):
            if pieceList[row][i] == data['otherPlayer']:
                pieceList[row][i] = data['player']
                print(True)
    
    
"""
def flipNorth(row,col):
    for row in pieceList:
        if row[clickCol] == color:
            sameCol = True
            break

def flipNorthWest(row,col):
    for i in range(-1*(min(clickCol,clickRow)),min(8-clickCol,8-clickRow)):
        if pieceList[clickRow+i][clickCol+i] == color:
            sameDiag1 = True
            break
    
def flipNorthEast(row,col):
    for i in range(-1*(min(clickCol,7-clickRow)),min(8-clickCol,clickRow)):
        if pieceList[clickRow-i][clickCol+i] == color:
            sameDiag2 = True
            break
"""        


if __name__ == '__main__':
    pieceList = []
    spriteList = []
    data = {}
    data['player'] = 1
    data['otherPlayer'] = 2
    
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
