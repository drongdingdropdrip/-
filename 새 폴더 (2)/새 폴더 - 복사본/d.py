import pygame
import os

pygame.init()

screen_x = 640
screen_y = 480
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("dongdong10's 3rd game")

running = True

clock = pygame.time.Clock() 

current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images") #이미지 폴더 위치 반환

background = pygame.image.load("background.png")

stage = pygame.image.load("stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1] #height높이  [1]은 높이

character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0] #폭
character_height = character_size[1]
character_x = (screen_x / 2) - (character_width / 2)
character_y = screen_y - character_height - stage_height

character_to_x = 0
character_speed = 10

weapon = pygame.image.load("weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapons = []
weapon_speed = 10

ball_images = [
    pygame.image.load("ball1.png"),
    pygame.image.load("ball2.png"),
    pygame.image.load("ball3.png"),
    pygame.image.load("ball4.png")
]
ball_speed_y = [-18, -15, -12, -9] #
balls = []

balls.append({
    "pos_x" : 50, #공의 x좌표 50
    "pos_y" : 50, #공의 y좌표 50
    "img_idx" : 0, #공에 이미지 인덱스
    "to_x" : 3,#x이동방향 -3이면 왼쪽 3이면 오른쪽
    "to_y" : -6, #y축 이동뱡향
    "init_spd_y" : ball_speed_y[0] #y 최초속도
})

while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            if event.key == pygame.K_UP:
                weapon_x = character_x + (character_width / 2) - (weapon_width / 2)
                weapon_y = character_y
                weapons.append([weapon_x, weapon_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    character_x += character_to_x
    if character_x < 0:
        character_x = 0
    elif character_x > screen_x - character_width:
        character_x = screen_x - character_width
    #무기 위치 조정
    weapons = [ [w[0], w[1]- weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > -20]

    for b_idx ,b_val in enumerate(balls):
        ball_x = b_val["pos_x"]
        ball_y = b_val["pos_y"]
        ball_img_idx = b_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #벽 다으면 위치변경(튕기기)
        if ball_x < 0 or ball_x > screen_x - ball_width:
            b_val["to_x"] *= -1
        if ball_y > screen_y - stage_height - ball_height:
            b_val["to_y"] = b_val["init_spd_y"]
        else:
            b_val["to_y"] += 0.5
        b_val["pos_x"] += b_val["to_x"]
        b_val["pos_y"] += b_val["to_y"]
        
    screen.blit(background, (0,0))
    for idx, val in enumerate(balls):
        ball_x = val["pos_x"]
        ball_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_x, ball_y))
    for weapon_x, weapon_y in weapons:
        screen.blit(weapon,(weapon_x, weapon_y))
    screen.blit(stage, (0,screen_y - stage_height))
    screen.blit(character, (character_x, character_y))
    pygame.display.update()