#########################
# IMPORTS
#########################

import os
from defaults import window, sprite

#########################
# TILES
#########################

class tile:
    def __init__(self,x,y,sprite_filename):
        self.x = x
        self.y = y
        self.sprite = sprite(sprite_filename)
    def render(self):
        self.sprite.render(False,self.x,self.y,30,30)

#########################
# MAP
#########################

class map:
    def __init__(self):
        self.matrix = []
    def gen(self,w,h):
        for index_y, y in enumerate(range(h)):
            self.matrix.append([])
            for x in range(w):
                self.matrix[index_y].append("")
    def render(self):
