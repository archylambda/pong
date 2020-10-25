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
        if self.pos.right > self.scr_width:
            self.pos.right = self.scr_width
        elif self.pos.left < 0:
            self.pos.left = 0;


    def set_dir(self, dir):
        if dir == -1 or dir == 0 or dir == 1:
            self.dir = dir

