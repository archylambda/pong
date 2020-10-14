class GameObject:

    def __init__(self, im, x, y, vx, vy):
        self.image = im
        self.pos = im.get_rect().move(x,y)
        self.speed_x = vx
        self.speed_y = vy

    def move(self):
        raise NotImplementedError



class Paddle(GameObject):

    def __init__(self, im, x, y, vy, scr_height):
        super().__init__(im, x, y, 0, vy)
        self.scr_height = scr_height
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
    pass


