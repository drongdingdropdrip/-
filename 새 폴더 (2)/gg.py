import pygame

pygame.init()

fluffybirdimg = pygame.image.load('player.png')
fluffybirdfifeimg = pygame.image.load('monster2.png')
fluffybirdstate = "down"

fluffybirdx = 10
fluffybirdy = 364

fluffybirdfifex = 10
fluffybirdfifey = 10

screen = pygame.display.set_mode((900, 800))
running = True

def fluffybird(x, y):
    screen.blit(fluffybirdimg, (x, y))
def fluffybirdfife(x, y):
    screen.blit(fluffybirdfifeimg, (x, y))
while running:
    screen.fill((193, 185, 184))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            fluffybirdy -= 1
    fluffybird(fluffybirdx, fluffybirdy)
    fluffybirdfife(fluffybirdfifex, fluffybirdfifey)
    fluffybirdy += 0.2
    pygame.display.update()