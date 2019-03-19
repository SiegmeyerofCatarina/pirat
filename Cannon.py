import numpy as np

from CannonBall import CannonBall
from Engine import Layer, Sprite
from KeyHandler import KeyHandler


class Cannon(KeyHandler, Layer):
    def __init__(self, spr_params, params):
        super(Cannon, self).__init__()
        self.params = params
        self.spr = Sprite(
            'res/ship_parts/cannon.png',
            rotation=spr_params['rotation'],
            position=spr_params['position'],
            anchor=(8, 12)
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
            'position': true_cannon_muzzle_position, #self.spr.point_to_world(self.spr.position),
            'speed': 200,
            'degrees': true_rotation,
            'ship_speed': ship_speed,
        }
        cannon_ball = CannonBall(params)
        self.add(cannon_ball.spr)
