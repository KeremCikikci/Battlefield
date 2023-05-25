from ursina import *

class Grass(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/grass/grass_tex.png', origin=(0, .5, 0)):#origin=5):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/grass/grass',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
            #origin_y = origin
        )