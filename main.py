import cocos

from Boat import Boat
from Sea import Sea
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

from KeyHandler import keyboard

director = cocos.director.director

if __name__ == "__main__":
    director.init(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption="Cocos Window")
    director.window.push_handlers(keyboard)

    boat_layer = Boat()
    sea_layer = Sea()

    world = cocos.scene.Scene()
    entity = cocos.scene.Scene()
    background = cocos.scene.Scene()
    background.add(sea_layer)

    world.add(background)
    world.add(entity)

    entity.add(boat_layer)

    director.run(world)
