#Shaylee McBride
#23May2018
#othello.py

#add a sign for whose turn it is
#add an endgame
#add comments
#"winner" function
#what is point of "flipPieces function

from ggame import *

BOX_SIZE = 70

#displays board, score, and current pieces in list
def buildBoard():
    #board
    for row in range(8):
        L = []
        for col in range(8):
            Sprite(box,(col*BOX_SIZE,row*BOX_SIZE))
            if pieceList[row][col] == 1:
                Sprite(blackCircle,(col*BOX_SIZE,row*BOX_SIZE))
            elif pieceList[row][col] == 2:  
                Sprite(whiteCircle,(col*BOX_SIZE,row*BOX_SIZE))
    
    #pieces            
    Sprite(TextAsset('Turn:'),(BOX_SIZE*8.2,BOX_SIZE*.4))
    if data['player'] == 1:
        Sprite(blackCircle,(BOX_SIZE*9,BOX_SIZE*.1))
    else:
        Sprite(whiteCircle,(BOX_SIZE*9,BOX_SIZE*.1))
    
    #score
    Sprite(TextAsset('Black: '+str(scoreList[0])+' White: '+str(scoreList[1])),(BOX_SIZE*8.2,BOX_SIZE*1.5))  
    
    #detects where mouse clicks, decides if it's legal, and calls flips
def mouseClick(event):
    #converts mouse x and y into columns and rows
    clickCol = int(event.x//BOX_SIZE)
    clickRow = int(event.y//BOX_SIZE)
    
    if clickRow > 7 or clickCol > 7 or pieceList[clickRow][clickCol] != '': #breaks if illegal move
        return False
    
    #calls functions to flip pieces
    w = flipWest(clickRow,clickCol)
    e = flipEast(clickRow,clickCol)
    n = flipNorth(clickRow,clickCol)
    s = flipSouth(clickRow,clickCol)
    nw = flipNorthWest(clickRow,clickCol)
    se = flipSouthEast(clickRow,clickCol)
    ne = flipNorthEast(clickRow,clickCol)
    sw = flipSouthWest(clickRow,clickCol)
    
    #if any of the pieces flipped, it's a legal move so update board and switch players
    if w == True or e == True or n == True or s == True or nw == True or se == True or ne == True or sw == True:
        pieceList[clickRow][clickCol] = data['player']
        data['player'] = 3 - data['player']
        data['otherPlayer'] = 3 - data['otherPlayer']
        updateScore()
        redrawAll()
        winner()

  
def flipWest(row,col):
    status = False
    for i in range(col-1,-1,-1):
        if pieceList[row][i] == '':
            break
        elif pieceList[row][i] == data['player']:
            for j in range(i,col):
                if pieceList[row][j] == data['otherPlayer']: #if other color
                    pieceList[row][j] = data['player'] #technically this doesn't need to be in this 'if' bc it's already determined that only the other color lies in this range
                    status = True #but I needed the status part to get rid of some illegal moves
            break
    return status

def flipEast(row,col):
    status = False
    for i in range(col+1,8):  #from the column after the clicked one to the end
        if pieceList[row][i] == '': #stop if encounter an empty cell
            break
        elif pieceList[row][i] == data['player']:  #if find another of same color
            for j in range(col+1,i):  #check between them
                if pieceList[row][j] == data['otherPlayer']:
                    pieceList[row][j] = data['player']  #flip
                    status = True
            break
    return status

def flipNorth(row,col):
    status = False
    for i in range(row-1,-1,-1):
        if pieceList[i][col] == '':
            break
        elif pieceList[i][col] == data['player']:  #if this row has a matching piece above in same column
            for j in range(i, row): #check between them for other color
                if pieceList[j][col] == data['otherPlayer']:
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
                if pieceList[j][col] == data['otherPlayer']:
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
                if pieceList[row-j][col-j] == data['otherPlayer']:
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
                if pieceList[row+j][col+j] == data['otherPlayer']:
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
                if pieceList[row+j][col-j] == data['otherPlayer']:
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
                if pieceList[row-j][col+j] == data['otherPlayer']:
                    pieceList[row-j][col+j] = data['player']
                    status = True
            break
    return status
    
def updateScore():
    black = 0
    white = 0
    for row in pieceList:
        black += row.count(1)
        white += row.count(2)
    scoreList[0] = black
    scoreList[1] = white

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    buildBoard()

def winner():
    for row in pieceList:
        for col in row:
            if col == '':
                break
            elif row == 7:
                if scoreList[0] > scoreList[1]:
                    print('Black Wins!')
                elif scoreList[0] < scoreList[1]:
                    print('White Wins!')
                else:
                    print('Tie Game!')

if __name__ == '__main__':
    pieceList = [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', 2, 1, '', '', ''], ['', '', '', 1, 2, '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']]
    scoreList = [2,2]
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
