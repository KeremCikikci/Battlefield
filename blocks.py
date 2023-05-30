from ursina import *
import uuid

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
        self.id = uuid.uuid1()

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
        self.id = uuid.uuid1()

class Sand(Button):
    def __init__(self, position=(0, 0, 0), texture='blocks/sand_tex.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/block',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )
        self.id = uuid.uuid1()

class Target(Button):
    def __init__(self, position, texture='blocks/target_tex.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/block',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )
        self.id = uuid.uuid1()