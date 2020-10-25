import sys, pygame
from gameobject import *


PADDLE_VEL = 1
SIZE = WIDTH, HEIGHT = 800, 600
BLACK_C = 0, 0, 0
BLOCK_IMAGE = 'block.bmp'


pygame.init()

screen = pygame.display.set_mode(SIZE)

paddle_im = pygame.image.load(BLOCK_IMAGE).convert()
player = Paddle(paddle_im, WIDTH // 2, HEIGHT - 30, PADDLE_VEL, SIZE)




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.set_dir(-1)
            elif event.key == pygame.K_x:
                player.set_dir(1)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_z, pygame.K_x):
                player.set_dir(0)

    player.move()

    screen.fill(BLACK_C)
    screen.blit(player.image, player.pos)
    pygame.display.flip()





