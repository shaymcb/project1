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
        w = flipWest(clickRow,clickCol)
        e = flipEast(clickRow,clickCol)
        n = flipNorth(clickRow,clickCol)
        s = flipSouth(clickRow,clickCol)
        nw = flipNorthWest(clickRow,clickCol)
        se = flipSouthEast(clickRow,clickCol)
        ne = flipNorthEast(clickRow,clickCol)
        sw = flipSouthWest(clickRow,clickCol)
        
        if w == True or e == True or n == True or s == True or nw == True or se == True or ne == True or sw == True:
            pieceList[clickRow][clickCol] = data['player']
            data['player'] = 3 - data['player']
            data['otherPlayer'] = 3 - data['otherPlayer']
            redrawAll()
  
#works
def flipWest(row,col):
    status = False
    for i in range(col-1,0,-1):
        if pieceList[row][i] == '':
            break
        elif pieceList[row][i] == data['player']:
            for j in range(i,col):
                pieceList[row][j] = data['player']
                status = True
            break
    return status

def flipEast(row,col):
    status = False
    for i in range(col+1,8):  #from the column after the clicked one to the end
        if pieceList[row][i] == '': #stop if encounter an empty cell
            break
        elif pieceList[row][i] == data['player']:  #if find another of same color
            for j in range(col+1,i):  #check between them
                pieceList[row][j] = data['player']  #flip
                status = True
            break
        """
    if data['player'] in pieceList[row][col:]: #same as above but for east
        pos = pieceList[row][col:].index(data['player']) + col
        for i in range(col,pos):
            if pieceList[row][i] == data['otherPlayer']:
                pieceList[row][i] = data['player']
                status = True
                """
    
    return status

def flipNorth(row,col):
    status = False
    for i in range(row-1,0,-1):
        if pieceList[i][col] == '':
            break
        elif pieceList[i][col] == data['player']:  #if this row has a matching piece above in same column
            for j in range(i, row): #check between them for other color
                pieceList[j][col] = data['player']
                status = True
            break
    return status


def flipSouth(row,col):
    status = False
    for i in range(row+1,8):
        if pieceList[i][col] == '':
            break
        elif pieceList[i][col] == data['player']:  #if this row has a matching piece below in same column
            for j in range(row+1,i): #check between them for other color
                pieceList[j][col] = data['player']
                status = True
            break
    return status
            


def flipNorthWest(row,col):
    status = False
    for i in range(1,min(col,row)+1):
        if pieceList[row-i][col-i] == '':
            break
        elif pieceList[row-i][col-i] == data['player']:
            for j in range(1,i):
                pieceList[row-j][col-j] = data['player']
                status = True
            break
    return status

def flipSouthEast(row,col):
    status = False
    for i in range(1,min(8-col,8-row)):
        if pieceList[row+i][col+i] == '':
            break
        elif pieceList[row+i][col+i] == data['player']:
            for j in range(1,i):
                pieceList[row+j][col+j] = data['player']
                status = True
            break
    return status
            


def flipSouthWest(row,col):
    status = False
    for i in range(1,min(col,7-row)):
        if pieceList[row+i][col-i] == '':
            break
        elif pieceList[row+i][col-i] == data['player']:
            for j in range(1,i):
                pieceList[row+j][col-j] = data['player']
                status = True
            break
    return status
       
       
def flipNorthEast(row,col):
    status = False
    for i in range(1,min(8-col,row)):
        if pieceList[row-i][col+i] == '':
            break
        elif pieceList[row-i][col+i] == data['player']:
            for j in range(1,i):
                pieceList[row-j][col+j] = data['player']
                status = True
            break
    return status


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
