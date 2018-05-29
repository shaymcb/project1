#Shaylee McBride
#23May2018
#othello.py

from ggame import *

BOX_SIZE = 70

#set board and starting position
def buildBoard():
    for row in range(8):
        L = []
        for col in range(8):
            Sprite(box,(col*BOX_SIZE,row*BOX_SIZE))
            if pieceList[row][col] == 1:
                spriteList.append(Sprite(blackCircle,(col*BOX_SIZE,row*BOX_SIZE)))
            elif pieceList[row][col] == 2:  
                spriteList.append(Sprite(whiteCircle,(col*BOX_SIZE,row*BOX_SIZE)))
  
    
def mouseClick(event):
    clickCol = int(event.x//BOX_SIZE)
    clickRow = int(event.y//BOX_SIZE)
    placed = False
    
    for i in range(-1*min(1,clickRow),min(2,7-clickRow)):
        for j in range(-1*min(1,clickCol),min(2,8-clickCol)):
            if pieceList[clickRow+i][clickCol+j] == data['otherPlayer'] and pieceList[clickRow][clickCol] == '':
                placed = True
    
    if placed == True:
        flipWest(clickRow,clickCol)
        flipEast(clickRow,clickCol)
        flipNorth(clickRow,clickCol)
        flipSouth(clickRow,clickCol)
        flipNorthWest(clickRow,clickCol)
        flipSouthEast(clickRow,clickCol)
        
        pieceList[clickRow][clickCol] = data['player']
        data['player'] = 3 - data['player']
        data['otherPlayer'] = 3 - data['otherPlayer']
        redrawAll()
  
#works
def flipWest(row,col):
    if data['player'] in pieceList[row][:col]: #if in the same row there is matching piece to the west
        pos = pieceList[row][:col].index(data['player']) #record its position
        for i in range(pos,col):        #and check between for other color
            if pieceList[row][i] == data['otherPlayer']:
                pieceList[row][i] = data['player']


def flipEast(row,col):
    if data['player'] in pieceList[row][col:]: #same as above but for east
        pos = pieceList[row][col:].index(data['player']) + col
        for i in range(col,pos):
            if pieceList[row][i] == data['otherPlayer']:
                pieceList[row][i] = data['player']


def flipNorth(row,col):
    for i in range(0,row):
        if pieceList[i][col] == data['player']:  #if this row has a matching piece above in same column
            for j in range(i, row): #check between them for other color
                if pieceList[j][col] == data['otherPlayer']:
                    pieceList[j][col] = data['player']
            break

def flipSouth(row,col):
    for i in range(row,8):
        if pieceList[i][col] == data['player']:  #if this row has a matching piece below in same column
            for j in range(row,i): #check between them for other color
                if pieceList[j][col] == data['otherPlayer']:
                    pieceList[j][col] = data['player']
            break


def flipNorthWest(row,col):
    for i in range(1,min(col,row)+1):
        if pieceList[row-i][col-i] == data['player']:
            for j in range(0,i):
                if pieceList[row-j][col-j] == data['otherPlayer']:
                    pieceList[row-j][col-j] = data['player']
            break

def flipSouthEast(row,col):
    for i in range(1,min(8-col,8-row)):
        if pieceList[row+i][col+i] == data['player']:
            for j in range(0,i):
                if pieceList[row+j][col+j] == data['otherPlayer']:
                    pieceList[row+j][col+j] = data['player']
            break

"""
def flipNorthEast(row,col):
    for i in range(-1*(min(clickCol,7-clickRow)),min(8-clickCol,clickRow)):
        if pieceList[clickRow-i][clickCol+i] == color:
            sameDiag2 = True
            break
"""        
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    buildBoard()


if __name__ == '__main__':
    pieceList = [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', 2, 1, '', '', ''], ['', '', '', 1, 2, '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']]
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
