from Engine import Sprite, Move


class CannonBall:
    def __init__(self, params):
        super(CannonBall, self).__init__()

        self.spr = Sprite(
            r'res/ship_parts/cannonBall.png',
            position=params['position'],
        )
        self.spr.velocity = params['ship_speed']
        self.spr.acceleration = (0, 0)
        self.spr.do(Ballistics(params))


class Ballistics(Move):
    def __init__(self, params):
        super(Ballistics, self).__init__(params)

    def start(self):
        self.target.rotation = self.params['degrees']
        self.target.velocity = (
            self.speed * self.velocity[0] + self.target.velocity[0],
            self.speed * self.velocity[1] + self.target.velocity[1]
        )
        air_resistance = 0.5
        self.target.acceleration = (
            - air_resistance * self.target.velocity[0],
            - air_resistance * self.target.velocity[1],
        )

    def step(self, dt):
        super().step(dt)
        if self.target.velocity[0] ** 2 + self.target.velocity[0] ** 2 < 1e4:
            self.target.kill()
