from ursina import *

class Grass(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/grass_tex.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/block',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )

class Stone(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/stone_tex.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/block',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )