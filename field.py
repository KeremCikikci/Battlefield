from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

fps = True
sen = 0.2

app = Ursina()

x_pos, y_pos, z_pos = 0, 2, -10
x_angle, y_angle, z_angle = 0, 0, 0
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)
window.fps_counter.enabled = True
window.exit_button.visible = True

blocks = [
    load_texture('assets/grass.png'),
]

#sky = Entity(
    # parent=scene,
    # model='sphere',
    # texture=load_texture('assets/dark_sky.jpg'),
    # scale=100,
    # double_sided=True
#)
sky = Entity(color=color.rgb(255,255,255), model='sphere', double_sided=True, scale=100)

tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex.png', y=1, x=1)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex1.png', y=1, x=2)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex2.png', y=1, x=3)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex3.png', y=1, x=4)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex4.png', y=1, x=5)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex5.png', y=1, x=6)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex6.png', y=1, x=7)
tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank_tex7.png', y=1, x=8)


def input(key):
    global fps
    if key == 'q':
        fps=False
    if key == 'e':
        fps=True

def update():
    global x_pos, y_pos, z_pos, x_angle, y_angle, z_angle, fps
    if fps:
        if held_keys['space']:
            y_pos += sen
        elif held_keys['shift']:
            y_pos -= sen
        camera.position = (camera.position[0], y_pos, camera.position[2])

    if fps and mouse.locked == False:
        mouse.locked = True
        mouse.visible = False
        camera.on_enable()
    if fps == False and mouse.locked:
        camera.on_disable()
        mouse.locked = False
        mouse.visible = True

class Ground(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass/grass_tex.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/grass/grass',
            #origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            #scale=0.5
        )

for z in range(10):
    for x in range(10):
        ground = Ground(position=(x, 0, z))

if fps:
    camera = FirstPersonController()
    camera.gravity = 0
    mouse.locked = True
    mouse.visible = False


app.run()