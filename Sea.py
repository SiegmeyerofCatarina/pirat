import cocos
import pyglet


class Sea(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        img = pyglet.image.load("res/sea.png")
        img_grid = pyglet.image.ImageGrid(img, 1, 16, item_height=512, item_width=512)
        animation_sprite = pyglet.image.Animation.from_image_sequence(img_grid[0:], 0.1)

        spr = [0] * 25
        for i in range(5):
            for j in range(5):
                tmp = i * 5 + j
                spr[tmp] = cocos.sprite.Sprite(animation_sprite)
                spr[tmp].position = i * 512, j * 512
                spr[tmp].velocity = (0, 0)
                # spr[tmp].do(Mover())
                self.add(spr[tmp])
