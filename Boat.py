from Cannon import Cannon
from Engine import Move, Layer, Sprite
from KeyHandler import KeyHandler
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Mover(Move):
    def __init__(self, params):
        super().__init__(params)

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

        self.spr = Sprite('res/ship_parts/hullLarge_1.png', scale=1)

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
            self.params,
        )

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
