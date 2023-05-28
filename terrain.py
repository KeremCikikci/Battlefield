from blocks import *
from ursina import *
from maps import dungeon

maps = {"dungeon": dungeon}

def vis_terrain(map_name):
    map_ = maps[map_name]
    for x in range(len(map_)):
        for z in range(len(map_[x])):
            if map_[x][z] == 1:
                Grass(position=(x,0,z))
            elif map_[x][z] == 1:
                Stone(position=(x,0,z))
            elif map_[x][z] == 2:
                Sand(position=(x,0,z))

def vis_rect_terrain(mLENGTH, mWIDTH):
    for z in range(mLENGTH):
        for x in range(mWIDTH):
            Grass(position=(x, 0, z))

def vis_co_sys():
    for z in range(-30, 300):
        a1=Entity(parent=scene, model='cube', color=color.white, scale=.1)
        a1.position=(0,0,z*.1)
    for x in range(-30, 300):
        a2=Entity(parent=scene, model='cube', color=color.red, scale=.1)
        a2.position=(x*.1,0,0)
    for y in range(-30, 300):
        a3=Entity(parent=scene, model='cube', color=color.yellow, scale=.1)
        a3.position=(0,y*.1,0)
