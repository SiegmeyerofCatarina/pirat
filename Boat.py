import math
import numpy as np

from Engine import Move, Layer, Sprite
from KeyHandler import KeyHandler
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Mover(Move):
    def __init__(self, params):
        super().__init__()
        self.params = params

    @property
    def speed(self):
        return self.params['speed']

    @property
    def angle(self):
        return self.params['degrees']

    @property
    def radian(self):
        return self.angle * np.pi / 180

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


class Boat(KeyHandler, Layer):
    def __init__(self):
        super(Boat, self).__init__()

        self.spr = Sprite(r"res/Ship parts/hullLarge_1.png", scale=1)

        # self.spr.anchor = self.spr.
        self.spr.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.rotate_speed = 10
        self.speed = 100
        self.spr.velocity = (0, 0)
        self.params = {
            'speed': 0,
            'degrees': 0,
            'turn_right': False,
            'turn_left': False,
            'turn_speed': 0.005
        }
        self.spr.do(Mover(self.params))
        self.cannon1 = Cannon(
            {
                'rotation': 90,
                'position': (self.spr.width / 4, 2),
            },
            self.params,
        )
        self.cannon2 = Cannon(
            {
                'rotation': -90,
                'position': (-self.spr.width / 4, 2),
            },
            self.params,)

        self.add(self.cannon1)
        self.spr.add(self.cannon1.spr)
        self.spr.add(self.cannon2.spr)
        self.add(self.spr)

        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.turn_right_start, self.turn_right_stop)
        self.key_handler('LEFT', self.turn_left_start, self.turn_left_stop)
        self.key_handler('SPACE', self.cannon1.fire)

        self.ball = None

    def turn_right_start(self):
        self.params['turn_right'] = True

    def turn_left_start(self):
        self.params['turn_left'] = True

    def go_up(self):
        self.params['speed'] += self.speed

    def go_down(self):
        self.params['speed'] -= self.speed

    def turn_right_stop(self):
        self.params['turn_right'] = False

    def turn_left_stop(self):
        self.params['turn_left'] = False


class CannonBall:
    def __init__(self, params):
        super(CannonBall, self).__init__()

        self.spr = Sprite(
            r'res/Ship parts/cannonBall.png',
            scale=1,
            position=params['position'],
        )
        self.spr.velocity = params['ship_speed']
        self.spr.do(Ballistics(params))


class Cannon(KeyHandler, Layer):
    def __init__(self, spr_params, params):
        super(Cannon, self).__init__()
        self.params = params
        self.spr = Sprite(
            'res/Ship parts/cannon.png',
            rotation=spr_params['rotation'],
            position=spr_params['position'],
        )

    def fire(self):
        print('fire')
        rho, phi = self.params['speed'], self.params['degrees']
        ship_speed = rho * np.sin(phi * np.pi / 180), rho * np.cos(phi * np.pi / 180)
        cannon_muzzle_position = np.array(self.spr.position) + np.array([self.spr.width / 2, 0])
        cannon_bottom_position = cannon_muzzle_position + np.array([0, self.spr.height])
        true_cannon_muzzle_position = self.spr.point_to_world(cannon_muzzle_position)
        true_cannon_bottom_position = self.spr.point_to_world(cannon_bottom_position)
        firedirection = - true_cannon_muzzle_position + true_cannon_bottom_position
        true_rotation = np.arctan2(*firedirection) * 180 / np.pi

        params = {
            'position': self.spr.point_to_world(self.spr.position),
            'speed': 50,
            'degrees': true_rotation,
            'ship_speed': ship_speed
        }
        cannon_ball = CannonBall(params)
        self.add(cannon_ball.spr)


class Ballistics(Mover):
    def __init__(self, params):
        super(Ballistics, self).__init__(params)

    def start(self):
        self.target.rotation = self.params['degrees']
        self.target.velocity = (
            self.speed * self.velocity[0] + self.target.velocity[0],
            self.speed * self.velocity[1] + self.target.velocity[1]
        )



    def step(self, dt):
        super(Mover, self).step(dt)

        # self.target.velocity = self.speed * self.velocity[0], self.speed * self.velocity[1]
