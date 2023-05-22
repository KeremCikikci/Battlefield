from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
app = Ursina()

text = Text(text="asdasdsd", color=color.rgb(255,0,0))
a = Entity(model='quad', position=(.5,.5), content=(
  text, text, text))

#print(wp.panel.scale_x)
#wp.x += wp.panel.scale_x / 4
# center = Entity(model='quad', scale=.1, color=color.red)
# p = Entity()
# for i in range(4*5):
#     b = Button(parent=p, model='quad', scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
#     b.text_entity.scale=1
# grid_layout(p.children, max_x=7, max_y=10, origin=(0, .5), spacing=(.15, 0))
# center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)


# wp = WindowPanel(
#     title="observer",
#     content=(
#         Text('Camera'),       
#         InputField(name='name_field'),
#         Button(text='Submit', color=color.azure),
#         Slider(),
#         Slider(),
#         ButtonGroup(('test', 'eslk', 'skffk'))
#         ),
#     )

# wp.right = 0

# center = Entity(model='quad', scale=.1, color=color.red)
# p = Entity()
# for i in range(4*5):
#   b = Button(parent=p, model='quad', scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
#   b.text_entity.scale=1
# t = time.time()
# grid_layout(p.children, max_x=7, max_y=10, origin=(0, .5), spacing=(.15, 0))
# center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)
# EditorCamera()
# print(time.time() - t)

# health_bar_1 = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=50)
# print(health_bar_1.text_entity.enabled, health_bar_1.text_entity.text)

# def input(key):
#   if key == '+' or key == '+ hold':
#     health_bar_1.value += 10
#   if key == '-' or key == '- hold':
#     health_bar_1.value -= 10
#     print('ow')

# rm = RadialMenu(
#   buttons = (
#     RadialMenuButton(text='1'),
#     RadialMenuButton(text='2'),
#     RadialMenuButton(text='3'),
#     RadialMenuButton(text='4'),
#     RadialMenuButton(text='5', scale=.5),
#     RadialMenuButton(text='6', color=color.red),
#     ),
#     enabled = False
#     )
# RadialMenuButton(text='6', color=color.red,x =-.5, scale=.06),
# def enable_radial_menu():
#   rm.enabled = True
# cube = Button(parent=scene, model='cube', color=color.orange, highlight_color=color.azure, on_click=enable_radial_menu)
# EditorCamera()

# DropdownMenu('File', buttons=(
#   DropdownMenuButton('New'),
#   DropdownMenuButton('Open'),
#   DropdownMenu('Reopen Project', buttons=(
#     DropdownMenuButton('Project 1'),
#     DropdownMenuButton('Project 2'),
#     )),
#     DropdownMenuButton('Save'),
#     DropdownMenu('Options', buttons=(
#       DropdownMenuButton('Option a'),
#       DropdownMenuButton('Option b'),
#       )),
#   DropdownMenuButton('Exit'),
#   ))

# gender_selection = ButtonGroup(('man', 'woman', 'other'))
# on_off_switch = ButtonGroup(('off', 'on'), min_selection=1, y=-.1, default='on', selected_color=color.red)

# def on_value_changed():
#     print('set gender:', gender_selection.value)
# gender_selection.on_value_changed = on_value_changed

# def on_value_changed():
#     print('turn:', on_off_switch.value)
# on_off_switch.on_value_changed = on_value_changed

# window.color = color._32

# default = Func(print, 'not yet implemented')

# def test(a=1, b=2):
#   print('------:', a, b)

# button_dict = {}
# for i in range(6, 20):
#   button_dict[f'button {i}'] = Func(print, i)

# bl = ButtonList(button_dict, font='VeraMono.ttf', button_height=1.5)
# def input(key):
#   if key == 'space':
#     bl.button_dict = {
#         'one' :     None,
#         'two' :     default,
#         'tree' :    Func(test, 3, 4),
#         'four' :    Func(test, b=3, a=4),
#     }

# background = Entity(model='quad', texture='pixelscape_combo', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.white)
# gradient = Entity(model='quad', texture='vertical_gradient', parent=camera.ui, scale=(camera.aspect_ratio,1), color=color.hsv(240,.6,.1,.75))

# username_field = InputField(y=-.12, limit_content_to='0123456789')
# password_field = InputField(y=-.18, hide_content=True)
# username_field.next_field = password_field

# def submit():
#     print('ursername:', username_field.text)
#     print('password:',  password_field.text)

# Button('Login', scale=.1, color=color.cyan.tint(-.4), y=-.26, on_click=submit).fit_to_text()
# username_field.on_value_changed = submit

# box = Entity(model='cube', origin_y=-.5, scale=1, color=color.orange)

# def scale_box():
#     box.scale_y = slider.value
#     box.scale_x = thin_slider.value
#     print(thin_slider.value)

# slider = Slider(0, 20, default=10, height=Text.size*3, y=-.4, step=1, on_value_changed=scale_box, vertical=True)

# thin_slider = ThinSlider(text='height', dynamic=True, on_value_changed=scale_box)

# thin_slider.label.origin = (0,0)
# thin_slider.label.position = (.25, -.1)


# tooltip_test = Tooltip(
# '<scale:1.5><pink>' + 'Rainstorm' + '<scale:1> \n \n' +
# '''Summon a <blue>rain
# storm <default>to deal 5 <blue>water
# damage <default>to <red>everyone, <default>including <orange>yourself. <default>
# Lasts for 4 rounds.'''.replace('\n', ' '),
#     background_color=color.red
# )

# tooltip_test.enabled = True

# Entity(model='plane', scale=8, texture='white_cube', texture_scale=(8,8))
# draggable_button = Draggable(scale=.1, text='drag me', position=(-.5, 0))
# world_space_draggable = Draggable(parent=scene, model='cube', color=color.azure, plane_direction=(0,1,0), lock=(1,0,0))

# EditorCamera(rotation=(30,10,0))
# world_space_draggable.drop = Func(print, 'dropped cube')


# descr = dedent('''
#   Rainstorm
#   Summon a rain storm to deal 5 water

#   damage to everyone, test including yourself.
#   1234 1234 1234 1234 1234 1234 2134 1234 1234 1234 1234 1234 2134 2134 1234 1234 1234 1234
#   Lasts for 4 rounds.''').strip()

# Text.default_resolution = 1080 * Text.size
# test = Text(text=descr, wordwrap=30)

# def input(key):
#   if key == 'a':
#       print('a')
#       test.text = '<default><image:file_icon> <red><image:file_icon> test '
#       print('by', test.text)

# window.fps_counter.enabled = False
# print('....', Text.get_width('yolo'))

app.run()