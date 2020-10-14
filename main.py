import sys, pygame
from gameobject import *

class GameController:
    PADDLE_VEL = 1
    BALL_VEL = 0.5
    SIZE = WIDTH, HEIGHT = 800, 600
    BLACK_C = 0, 0, 0

    PLAYER_1_SCORE = 0
    PLAYER_2_SCORE = 0
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(self.SIZE)

        paddle_im = pygame.image.load('platform.bmp').convert()
        self.player1 = Paddle(paddle_im, 10, self.HEIGHT // 2, GameController.PADDLE_VEL, self.SIZE)
        self.player2 = Paddle(paddle_im, self.WIDTH - 30, self.HEIGHT // 2, GameController.PADDLE_VEL, self.SIZE)

        ball_im = pygame.image.load('ball.bmp').convert()
        self.ball = Ball(ball_im, self.WIDTH // 2, self.HEIGHT // 2, 1, 1, self.SIZE)

        self.obj = [self.player1, self.player2, self.ball]


    def checkCollision(self):

        if self.ball.pos.colliderect(self.player1.pos) \
            or self.ball.pos.colliderect(self.player2.pos):
            self.ball.revSpeed()

    def run(self):
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

            #проверяем победителя
            winner = self.ball.isOffside()
            if winner:
                if winner == 1:
                    self.PLAYER_1_SCORE += 1
                else:
                    self.PLAYER_2_SCORE += 1
                self.ball.reset()
                continue


            self.screen.fill(GameController.BLACK_C)

            for elem in self.obj:
                self.screen.blit(elem.image, elem.pos)

            pygame.display.flip()

            pygame.time.delay(2)

if __name__ == '__main__':
    game = GameController()
    game.run()



