import imp
import random
import sys
import pygame
from pygame.locals  import *

FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY= SCREENHEIGHT*0.8
GAME_SPRITES ={}
GAME_SOUNDS={}
