import cocos


def load_map(world):
    map = cocos.tiles.load('res/map.tmx')
    world.add(map.contents.get('water'))
    world.add(map.contents.get('land'))
    return map
