import math

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
        self.cannon1 = Cannon('res/Ship parts/cannon.png',
                              rotation=90,
                              position=(self.spr.width/4, 2))
        self.cannon2 = Cannon('res/Ship parts/cannon.png',
                              rotation=-90,
                              position=(-self.spr.width/4, 2))

        self.spr.add(self.cannon1)
        self.spr.add(self.cannon2)
        self.add(self.spr)

        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.turn_right_start, self.turn_right_stop)
        self.key_handler('LEFT', self.turn_left_start, self.turn_left_stop)

        self.key_handler('SPACE', self.fire)

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

    def fire(self):
        print('fire')
        params = {'speed': 500,
                  'degrees': self.rotation + 90}
        self.ball = Shot(params)
        # self.ball.do(Ballistics(params))
        self.add(self.ball)


class Cannon(Sprite):
    def __init__(self, *args, **kwargs):
        super(Cannon, self).__init__(*args, **kwargs)


class Shot(Layer):
    def __init__(self, params):
        super(Shot, self).__init__()
        self.params = params
        self.kernel = Sprite(r'res/Ship parts/cannonBall.png', scale=100)
        self.kernel.velocity = params['speed']
        self.kernel.angle = params['degrees']
        self.velocity = (200, 200)


class Ballistics(Mover):
    def __init__(self, params):
        super().__init__(params)

    def step(self, dt):
        super(Mover, self).step(dt)
        self.target.rotation = self.params['degrees']
        self.target.velocity = self.speed * self.velocity[0], self.speed * self.velocity[1]
