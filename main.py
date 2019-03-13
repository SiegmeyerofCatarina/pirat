import sys
import cocos
from settings import RESOLUTION, WIDTH, HEIGHT
import pyglet
from pyglet.window import key

director = cocos.director.director
keyboard = key.KeyStateHandler()

class Keyboard1():

    is_event_handler = True

    def __init__(self):
        super(Keyboard1, self).__init__()
        self.__keysHandlers = dict()


    def on_key_press(self, key, modifiers):
        print(key, modifiers)
        if key in self.__keysHandlers and 'press' in self.__keysHandlers[key]:
            self.__keysHandlers[key]['press']()

    def on_key_release(self, key, modifiers):
        if key in self.__keysHandlers and 'release' in self.__keysHandlers[key]:
            self.__keysHandlers[key]['release']()

    def keyHadler(self, keyName, pressHandler=None, releaseHndler=None):
        keyNumber = getattr(key, keyName)
        self.__keysHandlers[keyNumber] = dict()
        if pressHandler:
            self.__keysHandlers[keyNumber]['press'] = pressHandler
        if releaseHndler:
            self.__keysHandlers[keyNumber]['release'] = releaseHndler


# class Keyboard():
#     def __init__(self,keyName):
#         self.keyMap = key.KeyStateHandler()
#         director.window.push_handlers(self.keyMap)
#         self.key = getattr(key, keyName)
#
#     # @property
#     def pressed(self):
#         return self.keyMap[self.key]


class Mover(cocos.actions.Move):
    def __init__(self, velocity):
        super().__init__()
        self.velocity = velocity


    def step(self, dt):
        super().step(dt)

        self.target.velocity = (self.velX, self.velY)


class Sea(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        img = pyglet.image.load("res/sea.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 16, item_height=512, item_width=512)
        amim = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1, loop=True)

        spr = [0] * 25
        for i in range(5):
            for j in range(5):
                tmp = i * 5 + j
                spr[tmp] = cocos.sprite.Sprite(amim)
                spr[tmp].position = i * 512, j * 512
                spr[tmp].velocity = (0, 0)
                # spr[tmp].do(Mover())
                self.add(spr[tmp])




class Boat(Keyboard1, cocos.layer.Layer):
    def __init__(self):
        super(Boat, self).__init__()
        # super(Keyboard, self).__init__()


        self.spr = cocos.sprite.Sprite("res/boat.png")

        size = director.get_window_size()
        self.spr.position = size[0] / 2, size[1] / 2
        self.speed = 200
        self.spr.velocity = (0, 0)
        self.velX = self.velY = 0
        spr.do(Mover())
        self.add(spr)
        self.keyHadler('UP', self.goUp)
        self.keyHadler('DOWN', self.goDown)
        self.keyHadler('RIGHT', self.goRight)
        self.keyHadler('LEFT', self.goLeft)




    def goRight(self):
        self.velX += self.speed

    def goLeft(self):
        self.velX -= self.speed

    def goUp(self):
        self.velY += self.speed

    def goDown(self):
        self.velY -= self.speed






class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Hell Cocos", font_name="Times New Roman", font_size=32,
                                 anchor_x="center", anchor_y="center")

        size = director.get_window_size()
        label.velocity = (0, 0)

        label.position = size[0] / 2, size[1] / 2

        # label.do(Mover())

        self.add(label)


if __name__ == "__main__":
    director.init(width=WIDTH, height=HEIGHT, caption="Cocos Window")
    director.window.push_handlers(keyboard)

    hello_layer = HelloCocos()
    boat_layer = Boat()
    sea_layer = Sea()

    world = cocos.scene.Scene()
    entity = cocos.scene.Scene()
    background = cocos.scene.Scene()
    background.add(sea_layer)

    world.add(background)
    world.add(entity)

    # scene0.add(hello_layer, 0)

    entity.add(boat_layer)


    director.run(world)
