import imp
import random
import sys
from turtle import Screen
import pygame
from pygame.locals  import *

FPS=33
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY= SCREENHEIGHT*0.8
GAME_SPRITES ={}
GAME_SOUNDS={}
PLAYER='gallery/sprites/bird.png'
BACKGROUND='gallery/sprites/background.png'
PIPE='gallery/sprites/pipe.png'
def welcomeScreen():
    """ Shows Welcome Screen """
    playrx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2
    messagex=int(SCREENWIDTH-GAME_SPRITES['message'].get_width())/2
    messagey=int(SCREENHEIGHT*0.13)
    basex=0 
    while True:
        for event in pygame.event.get():
            #if the user clicks on the cross button, close the game 
            if event.type==QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if user presses space or up key, start the game for them 
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0 ))
                SCREEN.blit(GAME_SPRITES['player'],( playrx, playery ))  
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey ))  
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY ))  
                pygame.display.update()
                FPSCLOCK.tick(FPS)      
def mainGame():
    score =0
    playerx= int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex=0

    # Create2 pipes for blitting on the screen
    newPipe1= getRandomPipe()
    newPipe2= getRandomPipe()
    # list of upper pipes
    upperPipes =[
        {'x':SCREENWIDTH+200 , 'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2) , 'y':newPipe1[0]['y']},
    ]
    #list of lower pipes
    lowerPipes=[
        {'x':SCREENWIDTH+200 , 'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2) , 'y':newPipe1[0]['y']},
    ]

    #pipe velocity 
    pipeVelX= -4
    playerVelY=-9
    playerMinVelY=-8
    playerMaxVelY=10
    playerAccY=1
    #velocity while flapping 
    playerFlapAccv=-8 
    playerFlapped=False # true only when its flapping 

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type ==KEYDOWN and (event.key == K_SPACE or event.key==K_UP):
                   if playery>0: #player is in the screen
                    playerVelY = playerFlapAccv
                    playerFlapped= True
                    GAME_SOUNDS['wing'].play()
        crashTest= isCollide(playerx,playery,upperPipes,lowerPipes) # does a crash test based on the given parameters
        # player is crashed 
        if crashTest:
            return
        # we are checking for the scrore and updating it and even printing 
        playerMidPos= playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos=pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<=playerMidPos < pipeMidPos+4:
                score+=1
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

        #increasing the velocity
        if playerVelY< playerMaxVelY and not playerFlapped:
            playerVelY +=playerAccY
        if playerFlapped:
            playerFlapped=False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery=playery+min(playerVelY,GROUNDY-playery-playerHeight)


        # moving the pipes to the left side 
        for upperPipe , lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] +=pipeVelX

         # add a new pipe when the first pipe is going out of the screen 
        if 0<upperPipes[0]['x'] <5:
            newpipe= getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen ,we are going to remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)  
        # here we are blitting our sprites 
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe, lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][0],(lowerPipe['x'],lowerPipe['y']))
            
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery)) 
        myDigits=[int(x) for x in list(str(score))]
        width = 0 
        for digits in myDigits:
            width+=GAME_SPRITES['numbers'][digits].get_width()
        Xoffset=(SCREENWIDTH- width )/2


        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREENHEIGHT*0.12))
            Xoffset+=GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)    
def isCollide(playerx,playery,upperPipes,Lowerpipes):
    return False                   


    
                

                






def getRandomPipe():
    """
    Generate posiitons of two pipes ( one bottom straight and one top rotated ) for blitting on the screen """ 
    pipeHeight= GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset+ random.randrange(0,int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()-1.2*offset))
    pipeX= SCREENWIDTH+10
    y1=pipeHeight - y2+ offset
    pipe = [
        {'x':pipeX, 'y':-y1},
        {'x':pipeX,'y':y2}
        ]
    return pipe
#Main Fucntions 
if __name__=="__main__":
    #here we are going to initialize the py game 
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird Game")
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
       pygame.image.load('gallery/sprites/1.png').convert_alpha(),
       pygame.image.load('gallery/sprites/2.png').convert_alpha(),
       pygame.image.load('gallery/sprites/3.png').convert_alpha(),
       pygame.image.load('gallery/sprites/4.png').convert_alpha(),

       pygame.image.load('gallery/sprites/5.png').convert_alpha(),

       pygame.image.load('gallery/sprites/6.png').convert_alpha(),
       pygame.image.load('gallery/sprites/7.png').convert_alpha(),
       pygame.image.load('gallery/sprites/8.png').convert_alpha(),
       pygame.image.load('gallery/sprites/9.png').convert_alpha(),


    )
GAME_SPRITES['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
GAME_SPRITES['base']=pygame.image.load('gallery/sprites/base.png').convert_alpha()
#dealing with the angles and the position of the pipes that are getting rendered
GAME_SPRITES['pipe']=(
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    pygame.image.load(PIPE).convert_alpha()
)
 # Game Sounds
GAME_SOUNDS['die']=pygame.mixer.Sound("gallery/audio/die.wav")
GAME_SOUNDS['hit']=pygame.mixer.Sound("gallery/audio/hit.wav")
GAME_SOUNDS['point']=pygame.mixer.Sound("gallery/audio/point.wav")
GAME_SOUNDS['swoosh']=pygame.mixer.Sound("gallery/audio/swoosh.wav")
GAME_SOUNDS['wing']=pygame.mixer.Sound("gallery/audio/wing.wav")


GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player']=pygame.image.load(PLAYER).convert()
while True:
    welcomeScreen() # this is my welcome screen 
    mainGame() # this is my main game function