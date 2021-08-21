from math import fabs
import pygame
import random

pygame.init()

icon = pygame.image.load('ddong.png')
pygame.display.set_icon(icon)

screen_x = 480
screen_y = 680
screen = pygame.display.set_mode((screen_x,screen_y))

ddong_img = pygame.image.load("ddong.png")
ddong_size = ddong_img.get_rect().size
ddong_sizex = ddong_size[0]
ddong_sizey = ddong_size[1]
ddong_y = 0
ddong_x = random.randint(0, screen_x - ddong_sizex)
ddong_fallspeed = 10

to_x = 0
to_y = 0

sprite = pygame.image.load("player2.png")
sprite_size = sprite.get_rect().size
sprite_sizex = sprite_size[0] 
sprite_sizey = sprite_size[1]
sprite_x = (screen_x / 2) - (sprite_sizex / 2)
sprite_y = (screen_y - sprite_sizey)

sprite_speed = 0.3

running = True

gamefps = pygame.time.Clock()

score = 0
score_font = pygame.font.Font(None, 40)

while running:
    dt = gamefps.tick(30)
    screen.fill((75, 83, 94))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= sprite_speed
            elif event.key == pygame.K_RIGHT:
                to_x += sprite_speed
            elif event.key == pygame.K_UP:
                ddong_fallspeed += 1          
            elif event.key == pygame.K_DOWN:
                ddong_fallspeed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    sprite_x += to_x * dt

    sprite_rect = sprite.get_rect()
    sprite_rect.left = sprite_x
    sprite_rect.top = sprite_y

    ddong_rect = ddong_img.get_rect()
    ddong_rect.left = ddong_x
    ddong_rect.top = ddong_y

    if sprite_x <= 0:
        sprite_x = 0
    if sprite_x >= screen_x - sprite_sizex:
        sprite_x = screen_x - sprite_sizex
    if ddong_y >= screen_y:
        ddong_y = 0
        ddong_x = random.randint(0, screen_x - ddong_sizex)
        score = score + 1
    ddong_y += ddong_fallspeed
    if sprite_rect.colliderect(ddong_rect):
        running = False
    screen.blit(sprite, (sprite_x, sprite_y))
    screen.blit(ddong_img, (ddong_x, ddong_y))
    sfr = score_font.render(str(score), True, (0,0,0))
    screen.blit(sfr,(10, 10))
    if ddong_fallspeed <= -1:
        # ddd = score_font.render("up", True, (19, 58, 175))
        # screen.blit(ddd, ((screen_x / 2)+50))
        pygame.time.delay(1000)
        running = False
    pygame.display.update()
# pygame.time.delay(1000)
