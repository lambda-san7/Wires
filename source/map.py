#########################
# IMPORTS
#########################

import os
from defaults import window, sprite, size

#########################
# TILES
#########################

class null_tile:
    def __init__(self):
        self.sprite = sprite(f"tiles/terminal.gif")
    def render(self,x,y):
        self.sprite.render(False,x,y,30,30)

#########################
# MAP
#########################

class map:
    def __init__(self,w):
        h = w
        self.matrix = []
        for index_y,y in enumerate(range(h)):
            self.matrix.append([])
            for x in range(w):
                self.matrix[index_y].append(null_tile())
    def render(self):
        x_coor = 0
        y_coor = 0
        for y in self.matrix:
            for x in y:
                x.render(x_coor,y_coor)
                x_coor += 30
            y_coor += 30
            x_coor = 0

world = map(size)