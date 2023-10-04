#########################
# IMPORTS
#########################

import pygame
import os
import random
import time
from defaults import window, event, sprite, center

#########################
# SCENES
#########################

def game():
    window.fill((0,0,0))
    sprite("tiles/terminal.gif").render(False, 100, 100, 30, 30)
    event()

scene = game

#########################
# LOOP
#########################

while True:
    scene()
    pygame.display.update()