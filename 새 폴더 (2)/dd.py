#불러오기
from typing import Collection
import pygame
import random
import math

#초기화
pygame.init()

#스크린 만들기
screen = pygame.display.set_mode((900, 800))
running = True

#기본설정
pygame.display.set_caption("dongdong10's game")
icon = pygame.image.load('game-icon.png')
pygame.display.set_icon(icon)
#나
playerimg = pygame.image.load('player.png') #그림은 32X32
playerX = 336
playerY = 700
playerx_change = 0
# 적
badimg = pygame.image.load('monster.png')
badX = random.randint(0, 835)
badY = random.randint(50, 400)
badx_change = 1
bady_change = 40
#배경화면 불러오기
background = pygame.image.load('bg.jpg')
# 총알 설정
ammoImg = pygame.image.load('ammo.png')
ammoX = 336
ammoY = 700
ammox_change = 1
ammoy_change = 3
ammo_state = "ready"

score = 0

#생명체 소환 함수
   #플레이어
def gamer(x, y):
    screen.blit(playerimg, (x, y))
   #적
def bad(x, y):
    screen.blit(badimg, (x, y))
   # 총알
def summon_ammo(x, y):
    global ammo_state
    ammo_state = "summon"
    screen.blit(ammoImg, (x+16, y+10))
def iscollision(ammox,ammoy,mobx,moby):
    distance = math.sqrt((math.pow(mobx-ammox,2)) + (math.pow(moby-ammoy, 2)))
    if distance < 27:
        return True
    else:
        return False
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    #창 X 표시로 끄게 하기
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            #좌우
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1.8
            if event.key == pygame.K_RIGHT:
                playerx_change = 1.8
            if event.key == pygame.K_UP:
                if ammo_state is "ready":
                    ammoX = playerX
                    summon_ammo(playerX, ammoY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    
    #플레이어 경계
    playerX += playerx_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 836:
        playerX = 836
    #적 튕기기
    badX += badx_change
    if badX <= 0.5:
        badx_change = 0.7
        badY += bady_change
    elif badX >= 835:
        badx_change = -0.7
        badY += bady_change
    #총알
    if ammoY <= 0:
        ammoY = 700
        ammo_state = "ready"
    if ammo_state is "summon":
        summon_ammo(ammoX, ammoY)
        ammoY -= ammoy_change
    Collection = iscollision(ammoX, ammoY, badX, badY)
    if Collection:
        ammoY = 700
        ammo_state = "ready"
        score += 1
        print(score)
        badX = random.randint(0, 835)
        badY = random.randint(50, 400)
    bad(badX, badY)
    gamer(playerX, playerY)
    pygame.display.update()