from ursina import *

app = Ursina()

terrain_entity = Entity(model=Terrain('heightmap_1', skip=8), scale=(40, 5, 20), texture='heightmap_1')
player = Entity(model='sphere', color=color.azure, scale=.2, origin_y=-.5)


hv = terrain_entity.model.height_values

def update():
    direction = Vec3(held_keys['d'] - held_keys['a'], 0, held_keys['w'] - held_keys['s'])
    player.position += direction * time.dt * 4

    player.y = terraincast(player.world_position, terrain_entity, hv)

EditorCamera()
Sky()
app.run()