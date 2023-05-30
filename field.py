from ursina import *
from npc import *
from blocks import *
from terrain import *
import random as rd
#from ui import *

mWIDTH, mLENGTH = 10, 10

npcs = []

app = Ursina()

EditorCamera()

x_pos, y_pos, z_pos = 17, 12, -14
x_angle, y_angle, z_angle = 30, -30, 0
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)

#renderUI(camera.position) #camera, npc list, selected npc

window.fps_counter.enabled = True
window.exit_button.visible = True
window.borderless = False

Sky()

#vis_terrain('dungeon')
vis_rect_terrain(10, 10)

vis_tanks('tank1', rd.randint(0, mWIDTH-1), rd.randint(0, mLENGTH-1))
vis_tanks('tank2', rd.randint(0, mWIDTH-1), rd.randint(0, mLENGTH-1))
vis_target((0, 1, 0))

app.run()