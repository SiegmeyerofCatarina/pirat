import cocos
import pyglet

from KeyHandler import KeyHandler
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Sprite(cocos.sprite.Sprite):
    def __init__(self, *args):
        super(Sprite, self).__init__(*args)

    def do(self, action, target=None):
        """Executes an :class:`.Action`.
        When the action is finished, it will be removed from the node's actions
        container.

        To remove an action you must use the :meth:`do` return value to
        call :meth:`remove_action`.

        Arguments:
            action (Action):
                Action that will be executed.
        Returns:
            Action: A clone of ``action``

        """
        a = action

        if target is None:
            a.target = self
        else:
            a.target = target

        a.start()
        self.actions.append(a)

        if not self.scheduled:
            if self.is_running:
                self.scheduled = True
                pyglet.clock.schedule(self._step)
        return a

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

