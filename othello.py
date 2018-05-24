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
        data['pieceList'].append('')
    
    data['pieceList'][4][3] = Sprite(blackCircle,(3*BOX_SIZE,4*BOX_SIZE))
    data['pieceList'][3][4] = Sprite(blackCircle,(4*BOX_SIZE,3*BOX_SIZE))
    data['pieceList'][4][4] = Sprite(whiteCircle,(4*BOX_SIZE,4*BOX_SIZE))
    data['pieceList'][3][3] = Sprite(whiteCircle,(3*BOX_SIZE,3*BOX_SIZE))


if __name__ == '__main__':
    data = {}
    data['pieceList'] = []
    green = Color(0x00FF00, 1)
    white = Color(0xFFFFFF, 1)
    black = Color(0x000000, 1)
    outline = LineStyle(1,black)
    
    box = RectangleAsset(BOX_SIZE,BOX_SIZE,outline,green)
    blackCircle  = CircleAsset(BOX_SIZE,outline,black)
    whiteCircle = CircleAsset(BOX_SIZE,outline,white)
    
    buildBoard()
    
    App().run()
