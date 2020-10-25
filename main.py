import sys, pygame
from gameobject import *


PADDLE_VEL = 1
BALL_VEL = 0.5
SIZE = WIDTH, HEIGHT = 800, 600
BLACK_C = 0, 0, 0

PLAYER_1_SCORE = 0


pygame.init()

screen = pygame.display.set_mode(SIZE)

paddle_im = pygame.image.load('platform.bmp').convert()
player1 = Paddle(paddle_im, 10, HEIGHT // 2, PADDLE_VEL, SIZE)




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.player1.set_dir(-1)
            elif event.key == pygame.K_z:
                self.player1.set_dir(1)
            elif event.key == pygame.K_UP:
                self.player2.set_dir(-1)
            elif event.key == pygame.K_DOWN:
                self.player2.set_dir(1)
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_z):
                self.player1.set_dir(0)
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                self.player2.set_dir(0)

    self.checkCollision()
    for elem in self.obj:
        elem.move()


    self.screen.fill(BLACK_C)

    for elem in self.obj:
        self.screen.blit(elem.image, elem.pos)

    pygame.display.flip()

    pygame.time.delay(2)





