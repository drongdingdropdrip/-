#불러오기
import pygame
import random
import math
from pygame import mixer

#초기화
pygame.init()
pygame.mixer.init()


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
badimg = []
badX = []
badY = []
badx_change = []
bady_change = []
num_of_bad = 6


for i in range(num_of_bad):
    badimg.append(pygame.image.load('monster.png'))
    badX.append(random.randint(0, 835))
    badY.append(random.randint(50, 300))
    badx_change.append(0.7)
    bady_change.append(40)
#배경화면 불러오기
background = pygame.image.load('happybg.jpg')
#소리
mixer.music.load('background.wav')
mixer.music.play(-1) #아니 저 -1값 1이나0으로 바꿔도 소리 나오는데 뭐임??

# 총알 설정
ammoImg = pygame.image.load('ammo.png')
ammoX = 336
ammoY = 700
ammox_change = 1
ammoy_change = 2
ammo_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',70)

gameover = 0

revive_font = pygame.font.Font('freesansbold.ttf',30)

#생명체 소환 함수
#플레이어
def gamer(x, y):
    screen.blit(playerimg, (x, y))
   #적
def bad(x, y, i):
    # if gameover == 0:    
    screen.blit(badimg[i], (x, y))
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
def seetext(x, y):
    # if gameover == 0:
    score = font.render("Score : " + str(score_value), True, (52, 210, 235))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (230, 300))
def screenfill_blit():
    screen.blit(background, (0, 0))
def notgameover():
    i = 0
    for j in range(num_of_bad):
        i = random.randint(50, 300)
        badY[j] = i
def revive_text():
    if gameover == 1:
        revive_text = revive_font.render("Press the 'R' key on your keyboard to respawn", True, (129, 0, 209))
        screen.blit(revive_text, (110, 500))
while running:
    screenfill_blit()
    #창 X 표시로 끄게 하기
    for event in pygame.event.get():    # 어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT:     # 창이 닫히는 이벤트(- ㅁ X 에서 X)가 발생했는가?
            running = False
            #좌우
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerx_change = 1.5
            if event.key == pygame.K_UP:
                if ammo_state is "ready":
                    fire_sound = mixer.Sound('laser.wav')
                    fire_sound.play()
                    ammoX = playerX
                    summon_ammo(playerX, ammoY)
            if event.key == pygame.K_r and gameover == 1:
                notgameover()
                score_value = 0
                textX = 10
                textY = 10
                gameover = 0
            if event.key == pygame.K_F4:
                running = False
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
    for i in range(num_of_bad):
        #game over

        if badY[i] >= 450:
            for j in range(num_of_bad):
                badY[j] = 2000
            screen.fill((75, 83, 94))
            game_over_text()
            gameover = 1
            revive_text()
            textY = 200
            textX = 380
            # break

        badX[i] += badx_change[i]
        if badX[i] <= 0.5:
            badx_change[i] = 0.7
            badY[i] += bady_change[i]
        elif badX[i] >= 835:
            badx_change[i] = -0.7
            badY[i] += bady_change[i]
        Collection = iscollision(ammoX, ammoY, badX[i], badY[i])
        if Collection:
            collection_sound = mixer.Sound('explosion.wav')
            collection_sound.play()
            ammoY = 700
            ammo_state = "ready"
            score_value += 1
            badX[i] = random.randint(0, 835)
            badY[i] = random.randint(50, 400)
        bad(badX[i], badY[i], i)
        # print(bady)
    #총알
    if ammoY <= 0:
        ammoY = 700
        ammo_state = "ready"
    if ammo_state is "summon":
        summon_ammo(ammoX, ammoY)
        ammoY -= ammoy_change
    gamer(playerX, playerY)
    seetext(textX, textY)
    pygame.display.update()