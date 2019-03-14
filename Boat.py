import cocos

from KeyHandler import KeyHandler
from Sprite import Sprite
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Mover(cocos.actions.Move):
    def __init__(self, vel):
        super().__init__()
        self.vel = vel

    def step(self, dt):
        super().step(dt)

        self.target.velocity = (self.vel['x'], self.vel['y'])
        print(self.vel['x'], self.vel['y'])


class Boat(KeyHandler, cocos.layer.Layer):
    def __init__(self):
        super(Boat, self).__init__()

        self.spr = Sprite("res/boat.png")

        self.spr.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.speed = 200
        self.spr.velocity = (0, 0)
        self.vel = {'x': 0, 'y': 0}
        self.spr.do(Mover(self.vel))
        self.add(self.spr)
        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.go_right)
        self.key_handler('LEFT', self.go_left)

    def go_right(self):
        self.vel['x'] += self.speed
        print(self.vel['x'], self.vel['y'])

    def go_left(self):
        self.vel['x'] -= self.speed

    def go_up(self):
        self.vel['y'] += self.speed

    def go_down(self):
        self.vel['y'] -= self.speed
