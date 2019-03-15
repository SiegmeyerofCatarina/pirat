import math

import cocos

from KeyHandler import KeyHandler
from Sprite import Sprite
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Mover(cocos.actions.Move):
    def __init__(self, params):
        super().__init__()
        self.params = params

    # @property
    # def x(self):
    #     return self.params['speed'] * math.cos(self.radian)
    #
    # @property
    # def y(self):
    #     return self.params['speed'] * math.sin(self.radian)

    @property
    def speed(self):
        return self.params['speed']

    @property
    def angle(self):
        return self.params['degrees']

    @property
    def radian(self):
        return self.angle * math.pi / 180

    @property
    def velocity(self):
        return (
            math.sin(self.radian),
            math.cos(self.radian),
        )

    def step(self, dt):
        super().step(dt)
        if self.speed:
            if self.params['turn_left']:
                self.params['degrees'] -= self.params['turn_speed'] * self.speed
            elif self.params['turn_right']:
                self.params['degrees'] += self.params['turn_speed'] * self.speed
        self.target.rotation = self.params['degrees']
        self.target.velocity = self.speed * self.velocity[0], self.speed * self.velocity[1]
        # print(self.x, self.y, self.params['degrees'])


class Boat(KeyHandler, cocos.layer.Layer):
    def __init__(self):
        super(Boat, self).__init__()

        self.spr = Sprite("res/boat.png", scale=0.2)

        # self.spr.anchor = self.spr.
        self.spr.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.rotate_speed = 10
        self.speed = 100
        self.spr.velocity = (0, 0)
        self.vel = {
            'speed': 0,
            'degrees': 0,
            'turn_right': False,
            'turn_left': False,
            'turn_speed': 0.005
        }
        self.spr.do(Mover(self.vel))
        self.add(self.spr)
        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.turn_right_start, self.turn_right_stop)
        self.key_handler('LEFT', self.turn_left_start, self.turn_left_stop)

    def turn_right_start(self):
        self.vel['turn_right'] = True

    def turn_left_start(self):
        self.vel['turn_left'] = True

    def go_up(self):
        self.vel['speed'] += self.speed

    def go_down(self):
        self.vel['speed'] -= self.speed

    def turn_right_stop(self):
        self.vel['turn_right'] = False

    def turn_left_stop(self):
        self.vel['turn_left'] = False
