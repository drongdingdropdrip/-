import pygame

#초기화
pygame.init()

#스크린 만들기
screen = pygame.display.set_mode((900, 900))
running = True


pygame.display.set_caption("dongdong10's game")
icon = pygame.image.load('game-icon.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('monster.png')
playerX = 420
playerY = 480
playerx_change = 0
playery_change = 0
def gamer(x, y):
    screen.blit(playerimg, (x, y))

while running:
    screen.fill((173, 216, 230))
    # playerX = playerX - 0.1
    # playerY = playerY - 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #좌우
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.5
            if event.key == pygame.K_UP:
                playery_change = -0.5
            if event.key == pygame.K_DOWN:
                playery_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerx_change = 0
    playerX = playerx_change + playerX
    playerY = playery_change + playery_change
    gamer(playerX, playerY)
    pygame.display.update()