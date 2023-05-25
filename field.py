from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from npc import *
from blocks import *
from ui import *

sen = 0.2

app = Ursina()

x_pos, y_pos, z_pos = 17, 7, -14
x_angle, y_angle, z_angle = 30, -30, 0
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)

renderUI(camera.position) #camera, npc list, selected npc

window.fps_counter.enabled = True
window.exit_button.visible = True
window.borderless = False

Sky()

for z in range(10):
    for x in range(10):
        ground = Grass(position=(x, 0, z))

app.run()