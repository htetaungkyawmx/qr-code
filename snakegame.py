import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#we will declare global constant definitions

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP":1 , "DOWN":2 , "LEFT":3 , "RIGHT":4}

#we will initialise screen
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)

#resource
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None,28)
game_over_font = score_numb_font
score_msg = score_font.render("Score : ",1,pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color =  pygame.Color(0,0,0)
black =   pygame.Color(0,0,0)

gameClock = pygame.time.Clock()

def checkCollision(posA,As ,posB,Bs):
    if(posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y):
        return True
    return False

def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if(snake.x <0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if(snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if(snake.y < 0):
        snake.y - SCREEN_HEIGHT - SNAKE_SIZE

class Apple:
    def _init_(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")

    def draw(self,screen:
             pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0))

class segment:
    self.x = x
    self.y = y
    self.direction = KEY["UP"]
    self.color = "white"

class snake:
    def _inint_(self,x,y);
        self.x = x
        self.y = y
        self.direction = key["UP"]
        self.stack = []
        self.stack.append(self)
        blackBox =  segment(self.x , self.y + SEPARATION)
        blackBox.direction   = KEY["UP"]
        blackBox.color = "NULL"
        self.stack.append(blackBox)  

        
def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    
            if event.type == pygame.K_UP:
               return KEY["UP"]
            elif event.key == pygame.K_DOWN:
               return KEY["DOWN"]
            elif event.type == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.type == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            #if we went to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
            #if we don't want to play game
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Gsme Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(320+12,240+40))      

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()                
        elif(mKey == "no"):
                break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)    

def drawScore(score):
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60,10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))

def drawGameTime(gameTime):
    game_time = score_font.render("Time:", 1, pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(game_time,(30,10))
    screen.blit(game_time_numb,(105,14))    

def exitScreen():
    pass

def main():
    score = 0
