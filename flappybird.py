import imp
import random
import sys
import pygame
from pygame.locals  import *

FPS=33
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY= SCREENHEIGHT*0.8
GAME_SPRITES ={}
GAME_SOUNDS={}
PLAYER='/gallery/sprites/bird.png'
BACKGROUND='/gallery/sprites/background.png'
PIPE='/gallery/sprites/pipe.png'

#Main Fucntions 
if __name__=="__main__":
    #here we are going to initialize the py game 
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird Game")
    GAME_SPRITES['numbers']=(
        pygame.image.load('/gallery/sprites/0.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/1.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/2.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/3.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/4.png').convert_alpha(),

       pygame.image.load('/gallery/sprites/5.png').convert_alpha(),

       pygame.image.load('/gallery/sprites/6.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/7.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/8.png').convert_alpha(),
       pygame.image.load('/gallery/sprites/9.png').convert_alpha(),


    )
GAME_SPRITES['message']=pygame.image.load('/gallery/aprites/message.png').convert_alpha()
GAME_SPRITES['base']=pygame.image.load('/gallery/aprites/message.png').convert_alpha()
#dealing with the angles and the position of the pipes that are getting rendered
GAME_SPRITES['pipe']=(
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    pygame.image.load(PIPE).convert_alpha()
)
abc