import cocos

from KeyHandler import KeyHandler
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Mover(cocos.actions.Move):
    def __init__(self):
        super().__init__()

    def step(self, dt):
        super().step(dt)

        self.target.velocity = (self.vel_x, self.vel_y)


class Boat(KeyHandler, cocos.layer.Layer):
    def __init__(self):
        super(Boat, self).__init__()

        self.spr = cocos.sprite.Sprite("res/boat.png")

        self.spr.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.speed = 200
        self.spr.velocity = (0, 0)
        self.vel_x = self.vel_y = 0
        # self.spr.do(Mover())
        self.add(self.spr)
        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.go_right)
        self.key_handler('LEFT', self.go_left)

    def go_right(self):
        self.vel_x += self.speed

    def go_left(self):
        self.vel_x -= self.speed

    def go_up(self):
        self.vel_y += self.speed

    def go_down(self):
        self.vel_y -= self.speed
