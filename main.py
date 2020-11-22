import sys, pygame
from gameobject import *

# game speed
GAME_SPEED = 60

# paddle settings
P_SPEED = 15
P_BOT_MARGIN = 30
# ball settings
BALL_SPEED = 8
# Screen settings
MENU_SIZE = 600, 400
GAME_SIZE = WIDTH, HEIGHT = 600, 800
DISPLAY_CAPTION = 'Arkanoid'
BLACK_C = 0, 0, 0
# block settings
B_TOP_MARGIN = HEIGHT // 20
B_LEFT_MARGIN = WIDTH // 20
B_CNT = 36
B_IN_ROW = 6
B_IMAGE = 'block.bmp'
B_SIZE = B_WIDTH, B_HEIGHT = 80, 20
B_HORIZ_DIST = 10
B_VERT_DIST = 10
#ball settings
BALL_IMAGE = 'ball.bmp'

# initialize pygame
pygame.init()

#screen = pygame.display.set_mode(SIZE)


class Arkanoid:

    def __init__(self):
        self._clock = pygame.time.Clock()

        #display settings
        pygame.display.set_mode(MENU_SIZE)
        pygame.display.set_caption(DISPLAY_CAPTION)
        pygame.mouse.set_visible(True)
        self._screen = pygame.display.get_surface()

        self._high_score = 0

        self._game = None
        self._start_screen = StartScreen()



    def main_loop(self):

        while True:
            # Game runs at 60 fps.
            self._clock.tick(GAME_SPEED)


            for event in pygame.event.get():
                # если нажата кнопка выхода
                if event.type == pygame.QUIT:
                    sys.exit()
                # если нахоимся в меню
                elif not self._game:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self._game = Game()
                # находимся в игре - обработка управления
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_z:
                            self._game.paddle_control(-1)
                        elif event.key == pygame.K_x:
                            self._game.paddle_control(1)
                    elif event.type == pygame.KEYUP:
                        if event.key in (pygame.K_z, pygame.K_x):
                            self._game.paddle_control(0)


            if not self._game:
                self._start_screen.show()
            else:
                self._game.update()
                #self._display_player_score(self._game.score)

                if self._game.over():
                #     if self._game.score > self._high_score:
                #         self._high_score = self._game.score
                #         self._display_high_score(self._high_score)
                #         save_high_score(self._high_score)
                    pygame.display.set_mode(MENU_SIZE)
                    self._game = None

            # Display all updates.
            pygame.display.flip()

class StartScreen:

    def __init__(self):
        self._screen = pygame.display.get_surface()

    def show(self):

        self._screen.fill(BLACK_C)
        logo_font = pygame.font.SysFont("Impact", 100)
        logo = logo_font.render("ARKANOID", 1, (255, 0, 0))
        self._screen.blit(logo, (95, 50))

        score_font = pygame.font.SysFont("3ds", 20)
        score = score_font.render("High Score: 15000", 1, (255, 255, 255))
        self._screen.blit(score, (200, 200))

        font = pygame.font.SysFont("Impact", 50)
        label = font.render("SPACEBAR TO START", 1 , (255, 255, 0))
        self._screen.blit(label, (95, 270))


class Game:

    def __init__(self):

        self._screen = pygame.display.set_mode(GAME_SIZE)

        self._lives = 3
        self._score = 0

        paddle_im = pygame.image.load(B_IMAGE).convert()
        self._paddle = Paddle(paddle_im, WIDTH // 2, HEIGHT - P_BOT_MARGIN, P_SPEED, GAME_SIZE)

        ball_im = pygame.image.load(BALL_IMAGE).convert()
        self._ball = Ball(ball_im, WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED, GAME_SIZE)

        self.blocks = []
        for i in range(B_CNT):
            im = pygame.image.load(B_IMAGE).convert()
            x = B_LEFT_MARGIN + i % B_IN_ROW * (B_WIDTH + B_HORIZ_DIST)
            y = B_TOP_MARGIN + i // B_IN_ROW * (B_HEIGHT + B_VERT_DIST)
            self.blocks.append(Block(im, x, y, GAME_SIZE))

    def paddle_control(self, dir):
        self._paddle.set_dir(dir)


    def over(self):
        return self._lives == 0

    def update(self):
        # пересчитываем положение мяча и платформы
        self._paddle.move()
        self._ball.move()

        # проверка столкновений
        if self._paddle.pos.colliderect(self._ball.pos):
            self._ball.rev_speed()

        # уничтожение блоков
        for block in self.blocks:
            if not block.is_destroyed() and self._ball.pos.colliderect(block.pos):
                self._ball.rev_speed()
                block.destroy()


        if self._ball.is_offside():
            self._ball.reset(BALL_SPEED)
            self._lives -= 1

        self._screen.fill(BLACK_C)
        for block in self.blocks:
            if not block.is_destroyed():
                self._screen.blit(block.image, block.pos)
        self._screen.blit(self._paddle.image, self._paddle.pos)
        self._screen.blit(self._ball.image, self._ball.pos)




if __name__ == '__main__':
    arkanoid = Arkanoid()
    arkanoid.main_loop()





