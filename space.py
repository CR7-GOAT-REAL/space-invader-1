import math 
import random
import pygame

from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800,500))
background = pygame.image.load("bg.png")

mixer.music.load("bg.wab")
mixer.music.play(-1)

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 380
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

bulletImg =  pygame.image.load("bullet.png")  
bulletX = 0
bulletY = 380
bulletX_change =  0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(X,Y):
    score = font.render("Score:" + str(score_value), True,(255,255,255))
    screen.blit(score,(X,Y))

def game_over_text():
    over_text = over_font.render("Game Over", True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(X,Y):
    screen.blit(playerImg,(X,Y))

def enemy(X,Y,i):
    screen.blit(enemyImg[i],(X,Y))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(X + 16, Y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)+(math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
    