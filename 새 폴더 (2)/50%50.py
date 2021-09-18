import pygame
import random

pygame.init()

screen_x = 700
screen_y = 600
screen = pygame.display.set_mode((screen_x,screen_y))

running = True

font = pygame.font.SysFont('Maplestory Bold.ttf', 100)
FFont = font.render("50%_game", True, (0,0,0))
fontx = 170
fonty = screen_x / 5

while running:
    screen.fill((100,100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(FFont, (fontx,fonty))
    pygame.display.update()