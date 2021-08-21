import pygame

pygame.init()
pygame.init()

screen_x = 480
screen_y = 680

sprite_speed = 0.5

screen = pygame.display.set_mode((screen_x,screen_y))

pygame.display.set_caption("my 2rd game")

background = pygame.image.load("2background.png")

sprite = pygame.image.load("player.png")
sprite_size = sprite.get_rect().size #저 위에있는 이미지 크기구함
sprite_sizex = sprite_size[0]   #<--가로크기[0]
sprite_sizey = sprite_size[1]   #<--세로크기[1]
sprite_x = (screen_x / 2) - (sprite_sizex / 2)
sprite_y = screen_y - sprite_sizey

enemy = pygame.image.load("monster.png")
enemy_size = enemy.get_rect().size #저 위에있는 이미지 크기구함
enemy_sizex = enemy_size[0]   #<--가로크기[0]
enemy_sizey = enemy_size[1]   #<--세로크기[1]
enemy_x = (screen_x / 2) - (enemy_sizex / 2)
enemy_y = (screen_y / 2) - (enemy_sizey / 2)

to_x = 0
to_y = 0

clock = pygame.time.Clock() #FPS

game_font =  pygame.font.Font(None, 40)
#시간
game_time = 10 + 1

start_time = pygame.time.get_ticks()

def player(x, y):
    screen.blit(sprite, (x,y))

def eneny(x, y):
    screen.blit(enemy, (x,y))

running = True

while running:
    dt = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= sprite_speed
            elif event.key == pygame.K_RIGHT:
                to_x += sprite_speed
            elif event.key == pygame.K_UP:
                to_y -= sprite_speed
            elif event.key == pygame.K_DOWN:
                to_y += sprite_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0
    sprite_x += to_x #* dt
    sprite_y += to_y #* dt

    if sprite_x < 0:
        sprite_x = 0
    if sprite_x > screen_x - sprite_sizex:
        sprite_x = screen_x - sprite_sizex
    if sprite_y < 0:
        sprite_y = 0
    if sprite_y > screen_y - sprite_sizey:
        sprite_y = screen_y - sprite_sizey
    
    #충돌 처리를 위한 rect 정보 업데이트
    sprite_rect = sprite.get_rect()   # 실제로 캐릭터 자체 이미지에 대한 렉트 정보는 항상 똑같은 위치를 가리키고 있다
    sprite_rect.left = sprite_x
    sprite_rect.top = sprite_y

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y

    if sprite_rect.colliderect(enemy_rect):
        running = False
    screen.blit(background, (0, 0))
    player(sprite_x, sprite_y)
    eneny(enemy_x, enemy_y)

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    #경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(game_time - elapsed_time)) , True , (0, 0, 0))
    screen.blit(timer, (10, 10))
    if game_time - elapsed_time <= 0:
        running = False
    pygame.display.update()
pygame.time.delay(1000)
pygame.quit()