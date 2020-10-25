from random import choice

class GameObject:
    scr_width = None
    scr_height = None

    def __init__(self, im, x, y, vx, vy, scr_size):
        self.image = im
        self.pos = im.get_rect().move(x,y)
        self.speed_x = vx
        self.speed_y = vy
        GameObject.scr_width = scr_size[0]
        GameObject.scr_height = scr_size[1]

    def move(self):
        raise NotImplementedError


class Paddle(GameObject):

    def __init__(self, im, x, y, vx, scr_size):
        super().__init__(im, x, y, vx, 0, scr_size)
        self.dir = 0

    def move(self):
        self.pos = self.pos.move(self.speed_x * self.dir, 0)
        if self.pos.right > self.scr_width:
            self.pos.right = self.scr_width
        elif self.pos.left < 0:
            self.pos.left = 0;


    def set_dir(self, dir):
        if dir == -1 or dir == 0 or dir == 1:
            self.dir = dir


class Ball(GameObject):

    def __init__(self, im, x, y, vx, vy, scr_size):
        super().__init__(im, x, y, vx, vy, scr_size)

    def move(self):
        self.pos = self.pos.move(self.speed_x, self.speed_y)
        if self.pos.top < 0:
            self.speed_y *= -1
            self.pos.top = 0
        elif self.pos.right > self.scr_width:
            self.speed_x *= -1
            self.pos.right = self.scr_width
        elif self.pos.left < 0:
            self.speed_x *= -1
            self.pos.left = 0


    def revSpeed(self):
        self.speed_y *= -1

    def IsOffside(self):
        return self.pos.bottom > self.scr_height

    def reset(self):
        self.pos.center = (self.scr_width // 2, self.scr_height // 2)
        self.speed_x = choice([-1, 1])
        self.speed_y = 1