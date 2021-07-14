#불러오기
import pygame
import random

#초기화
pygame.init()

#스크린 만들기
screen = pygame.display.set_mode((800, 600))
running = True

#기본설정
pygame.display.set_caption("dongdong10's game")
icon = pygame.image.load('game-icon.png')
pygame.display.set_icon(icon)
#나
playerimg = pygame.image.load('player.png')
playerX = 336
playerY = 500
playerx_change = 0
# 적
badimg = pygame.image.load('monster.png')
badX = random.randint(0, 800)
badY = random.randint(50, 200)
badx_change = 0.3
bady_change = 40
background = pygame.image.load('bg.jpg')

#생명체 소환 함수
def gamer(x, y):
    screen.blit(playerimg, (x, y))

def bad(x, y):
    screen.blit(badimg, (x, y))
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    #창 X 표시로 끄게 하기
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
            #좌우
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    
    #플레이어
    playerX += playerx_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #적
    badX += badx_change
    if badX <= 0:
        badx_change = 0.3
        badY += bady_change
    elif badX >= 736:
        badx_change = -0.3
        badY += bady_change
    bad(badX, badY)
    gamer(playerX, playerY)
    pygame.display.update()