from ursina import *
import random as rd
from npc import *
from blocks import *
#from ui import *

mWIDTH, mLENGTH = 10, 10

npcs = [['tank1', 0, 'tex_1_orange'], ['tank1', 0, 'tex_1_green'], ['tank1', 0, 'tex_1_lilac'], ['tank1', 0, 'tex_1_red'], 
        ['tank2', 0, 'tex_2_orange'], ['tank2', 0, 'tex_2_green'], ['tank2', 0, 'tex_2_lilac'], ['tank2', 0, 'tex_2_red'],
        ['tank3', 0, 'tex_3_orange'], ['tank3', 0, 'tex_3_green'], ['tank3', 0, 'tex_3_lilac'], ['tank3', 0, 'tex_3_red'],]

app = Ursina()

x_pos, y_pos, z_pos = 17, 12, -14
x_angle, y_angle, z_angle = 30, -30, 0
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)

#renderUI(camera.position) #camera, npc list, selected npc

window.fps_counter.enabled = True
window.exit_button.visible = True
window.borderless = False

Sky()

for z in range(mLENGTH):
    for x in range(mWIDTH):
        ground = Grass(position=(x, 0, z))

### Render NPCS
for i in range(len(npcs)):
    if npcs[i][1] == 0:
        Tank(npcs[i][0], position=(rd.randint(0, mWIDTH-1), 1, rd.randint(0, mLENGTH-1)), texture=npcs[i][2])

app.run()