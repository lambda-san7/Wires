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
    window.fill((0,0,0))
    world.render()
    event()

scene = game

#########################
# LOOP
#########################

while True:
    scene()
    pygame.display.update()