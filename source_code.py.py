import pygame
import random
import math
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((1000,700))
background=pygame.image.load('fruitGarder.JFIF')
mixer.music.load('background.wav')
mixer.music.play(-1)
pygame. display.set_caption("Apple Shooter")
icon=pygame.image.load("console.png")
pygame.display.set_icon(icon)
playerI=pygame.image.load("shooter1.png")
playerX=900
playerY=450
def player(x,y):
    screen.blit(playerI,(x,y))
appleI=[]
appleX=[]
appleY=[]
move1=[]
for i in range(0,10):
    appleI.append(pygame.image.load("apple.png"))
    appleX.append(random.randint(0,200))
    appleY.append(random.randint(100,500))
    move1.append(0.7)
def apple(x,y,i):
    screen.blit(appleI[i],(x,y))
bulletI=pygame.image.load('bullet.png')
bulletX=880
bulletY=450
state=False
score=0
positionX=860
positionY=12
def scoreV(x,y):
    font=pygame.font.SysFont(None,38)
    scoreR=font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(scoreR,(x,y))
def bullet(x,y):
    global state
    state=True
    screen.blit(bulletI,(x,y))
def isCollision(appleX,appleY,bulletX,bulletY):
    distance=math.sqrt(((appleX-bulletX)*(appleX-bulletX))+((appleY-bulletY)*(appleY-bulletY)))
    if(distance<27):
        return True
    return False
def game_over_text():
    game_font=pygame.font.SysFont(None,120)
    game_over=game_font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over,(200,330))
flag=True
move=1.8
move2=-5
while flag:
    screen.fill((255, 207, 207))
    screen.blit(background,(0,0))
    scoreV(positionX,positionY)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False
            break
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                move=1.8
            elif event.key==pygame.K_UP:
                move=-1.8
            elif event.key==pygame.K_SPACE:
                if(state==False):
                    bullet_sound=mixer.Sound('bullet.wav')
                    bullet_sound.play()
                    bulletY=playerY
                    bullet(bulletX,bulletY)
    playerY=(playerY+move)%700
    player(playerX,playerY)
    for i in range(0,10):
        if(appleX[i]>=860):
            game_over=mixer.Sound('game_over.wav')
            game_over.play()
            game_over_text()
            for j in range(0,10):
                appleY[j]=800
            move=0
            break
        if(appleY[i]>=700):
            move1[i]=-1
            appleX[i]=appleX[i]+30
        if(appleY[i]<=0):
            move1[i]=1
            appleX[i]=appleX[i]+30
        appleY[i]=appleY[i]+move1[i]
        if(isCollision(appleX[i],appleY[i],bulletX,bulletY)==True):
            collision_sound=mixer.Sound('apple.wav')
            collision_sound.play()
            bulletX=880
            state=False
            score+=1
            appleX[i]=random.randint(0,200)
            appleY[i]=random.randint(100,500)
        apple(appleX[i],appleY[i],i)
    if(bulletX<=0):
        bulletX=880
        state=False
    if(state==True):
        bullet(bulletX,bulletY)
        bulletX=bulletX+move2
    pygame.display.update()

