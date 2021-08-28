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

# background = pygame.image.load(os.path.join(image_path ,"background.png"))
background = pygame.image.load("background.png")
#background = pygame.image.load(os.path.join(image_path, "background.png"))

while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    pygame.display.update()