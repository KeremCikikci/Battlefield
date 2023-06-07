from blocks import *
import npc
from ursina import *
from maps import dungeon

maps = {"dungeon": dungeon}

blocks = []

npcs = []

def vis_terrain(map_name):
    map_ = maps[map_name]
    for x in range(len(map_)):
        for z in range(len(map_[x])):
            if map_[x][z] > 0 and map_[x][z] < 3:
                block = None
                if map_[x][z] == 1:
                    block = Grass(position=(x,0,z))
                elif map_[x][z] == 1:
                    block = Stone(position=(x,0,z))
                elif map_[x][z] == 2:
                    block = Sand(position=(x,0,z))
                blocks.append(block)

def vis_rect_terrain(mLENGTH, mWIDTH):
    for z in range(mLENGTH):
        for x in range(mWIDTH):
            block = Grass(position=(x, 0, z))
            #blocks.append(block)

def vis_co_sys():
    # Error
    for z in range(-30, 300):
        a1=Entity(parent=scene, model='cube', color=color.white, scale=.1)
        a1.position=(0,0,z*.1)
    for x in range(-30, 300):
        a2=Entity(parent=scene, model='cube', color=color.red, scale=.1)
        a2.position=(x*.1,0,0)
    for y in range(-30, 300):
        a3=Entity(parent=scene, model='cube', color=color.yellow, scale=.1)
        a3.position=(0,y*.1,0)

def vis_tanks(name, x, z):
    npc_ = npc.Tank(name, x=x, z=z)
    npcs.append(npc_)

def vis_target(position):
    target = Target(position)
    blocks.append(target)

def destroy_(obj, type):
    if type == 'npc':
        npcs.remove(obj)
    if type == 'block':
        blocks.remove(obj)
    destroy(obj)