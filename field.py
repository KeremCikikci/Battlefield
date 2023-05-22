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

sky = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assets/dark_sky.jpg'),
    scale=100,
    double_sided=True
)

tank = Entity(model='npcs/tank/tank', texture='npcs/tank/tank.png')

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
    if fps == False and mouse.locked:
        camera.on_disable()
        mouse.locked = False
        mouse.visible = True

class Ground(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.6, 1.0)),
            scale=0.5
        )

for z in range(10):
    for x in range(10):
        ground = Ground(position=(x, 0, z))

if fps:
    camera = FirstPersonController()
    camera.gravity = 0
    mouse.locked = True
    mouse.visible = False


b = Button(text='hello world!', color=color.azure, icon='sword', scale=1, text_origin=(-.5,0))
b.on_click = application.quit # assign a function to the button.
b.tooltip = Tooltip('exit')

#wp = WindowPanel()

# wp = WindowPanel(
#     title='Custom Window',
#     content=(
#         Text('Name:'),
#         InputField(name='name_field'),
#         Button(text='Submit', color=color.azure),
#         Slider(),
#         Slider(),
#         ButtonGroup(('test', 'eslk', 'skffk'))
#         ),
#     )
# wp.y = wp.panel.scale_y / 2 * wp.scale_y

app.run()