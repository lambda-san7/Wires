#########################
# IMPORTS
#########################

import pygame
import os
import random
import time
from defaults import window, event, sprite, center
from map import world

#########################
# SCENES
#########################

def game():
    window.fill((120,255,120))
    world.render()
    event()

scene = game

#########################
# LOOP
#########################

while True:
    scene()
    sprite("hammer.gif").render(False,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],30,30)
    pygame.display.update()