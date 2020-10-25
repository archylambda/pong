import sys, pygame
from gameobject import *


# paddle settings
P_VEL = 4
P_BOT_MARGIN = 30
# ball settings
BALL_VEL = 1
# Screen settings
SIZE = WIDTH, HEIGHT = 800, 600
BLACK_C = 0, 0, 0
# block settings
B_TOP_MARGIN = HEIGHT // 20
B_LEFT_MARGIN = WIDTH // 20
B_CNT = 32
B_IN_ROW = 8
B_IMAGE = 'block.bmp'
B_SIZE = B_WIDTH, B_HEIGHT = 80, 20
B_HORIZ_DIST = 10
B_VERT_DIST = 10
#ball settings
BALL_IMAGE = 'ball.bmp'

pygame.init()

screen = pygame.display.set_mode(SIZE)

paddle_im = pygame.image.load(B_IMAGE).convert()
player = Paddle(paddle_im, WIDTH // 2, HEIGHT - P_BOT_MARGIN, P_VEL, SIZE)

ball_im = pygame.image.load(BALL_IMAGE).convert()
ball = Ball(ball_im, WIDTH // 2, HEIGHT // 2, BALL_VEL, BALL_VEL, SIZE)

blocks = []
for i in range(B_CNT):
    im = pygame.image.load(B_IMAGE).convert()
    x = B_LEFT_MARGIN + i % B_IN_ROW * (B_WIDTH + B_HORIZ_DIST)
    y = B_TOP_MARGIN + i // B_IN_ROW * (B_HEIGHT + B_VERT_DIST)
    blocks.append(Block(im, x, y, SIZE))

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
    ball.move()

    if player.pos.colliderect(ball.pos):
        ball.revSpeed()

    for block in blocks:
        if not block.isDestroyed() and ball.pos.colliderect(block.pos):
            ball.revSpeed()
            block.destroy()

    if ball.IsOffside():
        ball.reset()

    screen.fill(BLACK_C)
    for block in blocks:
        if not block.isDestroyed():
            screen.blit(block.image, block.pos)
    screen.blit(player.image, player.pos)
    screen.blit(ball.image, ball.pos)
    pygame.display.flip()

    pygame.time.delay(2)





