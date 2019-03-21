import cocos

from settings import WINDOW_WIDTH, WINDOW_HEIGHT
director = cocos.director.director
director.init(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, caption="Cocos Window", autoscale=False, resizable=True)

from Scroller import scroller

from Boat import Boat
from KeyHandler import keyboard


if __name__ == "__main__":
    director.window.push_handlers(keyboard)

    boat_layer = Boat()

    map = cocos.tiles.load('res/map.tmx')
    scroller.add(map.contents.get('water'))
    scroller.add(map.contents.get('land'))
    scroller.add(boat_layer)

    scene = cocos.scene.Scene()
    scene.add(scroller)

    director.run(scene)
