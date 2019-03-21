from Cannon import Cannon
from Engine import Move, Layer, Sprite
from KeyHandler import KeyHandler
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from Scroller import scroller


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
        scroller.set_focus(self.target.x, self.target.y)


class Boat(KeyHandler, Layer):
    def __init__(self):
        super(Boat, self).__init__()



        self.spr = Sprite('res/ship_parts/hullLarge_1.png')

        self.cannon_slots = (
            {
                'position': (13 - self.spr.image_anchor_x, 56 - self.spr.image_anchor_y),
                'rotation': -90,
                'cannon': None,
            },
            {
                'position': (37 - self.spr.image_anchor_x, 56 - self.spr.image_anchor_y),
                'rotation': 90,
                'cannon': None,
            },
            {
                'position': (13 - self.spr.image_anchor_x, 38 - self.spr.image_anchor_y),
                'rotation': -90,
                'cannon': None,
            },
            {
                'position': (37 - self.spr.image_anchor_x, 38 - self.spr.image_anchor_y),
                'rotation': 90,
                'cannon': None,
            },
        )

        # self.spr.anchor = self.spr.
        self.spr.position = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
        self.rotate_speed = 10
        self.speed_step = 20
        self.speed_max = 150
        self.spr.velocity = (0, 0)
        self.spr.acceleration = (0, 0)
        self.params = {
            'speed': 0,
            'degrees': 0,
            'turn_right': False,
            'turn_left': False,
            'turn_speed': 0.005
        }
        self.spr.do(Mover(self.params))


        for i in range(4):
            slot = self.get_empty_slot()
            if not slot:
                break
            cannon = Cannon(slot, self.params)
            self.cannon_add(slot, cannon)
            self.key_handler('SPACE', cannon.fire)



        self.add(self.spr)

        self.key_handler('UP', self.go_up)
        self.key_handler('DOWN', self.go_down)
        self.key_handler('RIGHT', self.turn_right_start, self.turn_right_stop)
        self.key_handler('LEFT', self.turn_left_start, self.turn_left_stop)

    def turn_right_start(self):
        self.params['turn_right'] = True

    def turn_left_start(self):
        self.params['turn_left'] = True

    def go_up(self):
        self.params['speed'] += self.speed_step

    def go_down(self):
        self.params['speed'] -= self.speed_step

    def turn_right_stop(self):
        self.params['turn_right'] = False

    def turn_left_stop(self):
        self.params['turn_left'] = False

    def cannon_add(self, slot, cannon):
        slot['cannon'] = cannon
        self.add(cannon)
        self.spr.add(cannon.spr)

    def get_empty_slot(self):
        for slot in self.cannon_slots:
            if not slot['cannon']:
                return slot


