from Engine import Sprite, Move


class CannonBall:
    def __init__(self, params):
        super(CannonBall, self).__init__()

        self.spr = Sprite(
            r'res/ship_parts/cannonBall.png',
            scale=1,
            position=params['position'],
        )
        self.spr.velocity = params['ship_speed']
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

