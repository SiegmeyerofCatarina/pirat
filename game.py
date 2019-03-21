import cocos
from KeyHandler import keyboard
from map import load_map
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

director = cocos.director.director
director.init(
    width=WINDOW_WIDTH,
    height=WINDOW_HEIGHT,
    caption="Cocos Window",
    autoscale=False,
    resizable=True,
)

director.window.push_handlers(keyboard)

world = cocos.layer.ScrollingManager()
load_map(world)

scene = cocos.scene.Scene()
scene.add(world)


def game_start():
    director.run(scene)
