import sys, pygame
from gameobject import *

pygame.init()

PLATFORM_VELOCITY = 1

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
white = 255, 255, 255



screen = pygame.display.set_mode(size)

paddle_im = pygame.image.load('platform.bmp').convert()
player1 = Paddle(paddle_im, 10, height//2, PLATFORM_VELOCITY, height)
player2 = Paddle(paddle_im, width - 30, height//2, PLATFORM_VELOCITY, height)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.set_dir(-1)
            elif event.key == pygame.K_z:
                player1.set_dir(1)
            elif event.key == pygame.K_UP:
                player2.set_dir(-1)
            elif event.key == pygame.K_DOWN:
                player2.set_dir(1)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_z):
                player1.set_dir(0)
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player2.set_dir(0)


    player1.move()
    player2.move()

    screen.fill(black)
    screen.blit(player1.image, player1.pos)
    screen.blit(player2.image, player2.pos)
    pygame.display.flip()