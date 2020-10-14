import random

class GameObject:
    scr_width = None
    scr_height = None

    def __init__(self, im, x, y, vx, vy, scr_size):
        self.image = im
        self.pos = im.get_rect().move(x,y)
        self.speed_x = vx
        self.speed_y = vy
        self.scr_width = scr_size[0]
        self.scr_height = scr_size[1]

    def move(self):
        raise NotImplementedError


class Paddle(GameObject):

    def __init__(self, im, x, y, vy, scr_size):
        super().__init__(im, x, y, 0, vy, scr_size)
        self.dir = 0

    def move(self):
        self.pos = self.pos.move(0, self.speed_y * self.dir)
        if self.pos.bottom > self.scr_height:
            self.pos.bottom = self.scr_height
        elif self.pos.top < 0:
            self.pos.top = 0;


    def set_dir(self, dir):
        if dir == -1 or dir == 0 or dir == 1:
            self.dir = dir


class Ball(GameObject):

    def __init__(self, im, x, y, vx, vy, scr_size):
        super().__init__(im, x, y, vx, vy, scr_size)

    def move(self):
        self.pos = self.pos.move(self.speed_x, self.speed_y)
        if self.pos.bottom > self.scr_height:
            self.speed_y *= -1
            self.pos.bottom = self.scr_height
        elif self.pos.top < 0:
            self.speed_y *= -1
            self.pos.top = 0

    def revSpeed(self):
        self.speed_x *= -1

    def isOffside(self):
        """return winner player or 0 """
        if self.pos.right > self.scr_width:
            return 1
        if self.pos.left < 0:
            return 2;
        return 0

    def reset(self):
        self.pos.center = (self.scr_width // 2, self.scr_height // 2)
        speed = [-1, 1]
        self.speed_x = random.choice(speed)
        self.speed_y = random.choice(speed)
