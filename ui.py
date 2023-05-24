from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
app = Ursina()

window.borderless = False

Sky()

Panel = Entity(model='quad', origin=(-.5, .5), position=(.5, .5), scale=(.4, 1), color=color.dark_gray, parent=camera.ui)

CamGroup = Button(model='quad', origin=(-.5, .5), position=(.05, -.05), scale=(.4, .03), text="Camera", text_color=color.dark_gray, color=color.azure, parent=Panel)

CamCoorGroup = Entity(model='quad', origin=(-.5, .5), position=(CamGroup.x, CamGroup.y - CamGroup.scale_y), scale=(.87, .05), color=color.azure, parent=Panel)

#username_field = InputField(y=-.12, limit_content_to='0123456789')

CamXCoor = InputField(model='quad', character_limit=6, max_lines=1, size=.025, text_origin=(-.5,.5), origin=(-.5, .5), position=(.05, -.3), scale_x=.25, scale_y=.5, parent=CamCoorGroup)
#CamXCoor = InputField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(.05, -.3), scale=(.25, .5), parent=CamCoorGroup)
#CamYCoor = TextField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(CamXCoor.x + CamXCoor.scale_x + .05, CamXCoor.y), scale=(.25, .5), parent=CamCoorGroup)
#CamZCoor = TextField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(CamYCoor.x + CamYCoor.scale_x + .05, CamXCoor.y), scale=(.25, .5), parent=CamCoorGroup)

Selector = DropdownMenu('select', text_origin=(-1.05, 1.6), model='quad', origin=(-.5, .5), position=(CamCoorGroup.x, CamCoorGroup.y - CamCoorGroup.scale_y - .02), scale=(CamCoorGroup.scale_x, .04), color=color.azure, parent=Panel, 
                        buttons=(DropdownMenuButton('New', color=color.light_gray),))

NpcGroup = Entity(model='quad', origin=(-.5, .5), position=(Selector.x, Selector.y - Selector.scale_y - .01), scale=(Selector.scale_x, .3), color=color.azure, parent=Panel)

#NpcXCoor = TextField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(CamXCoor.x, -.05), scale=(.25, .1), parent=NpcGroup)
#NpcYCoor = TextField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(NpcXCoor.x + NpcXCoor.scale_x + .05, NpcXCoor.y), scale=(.25, .1), parent=NpcGroup)
#NpcZCoor = TextField(model='quad', character_limit=7, max_lines=1, origin=(-.5, .5), position=(NpcYCoor.x + NpcYCoor.scale_x + .05, NpcYCoor.y), scale=(.25, .1), parent=NpcGroup)

#showLinesText = Text('Show Lines', parent=NpcGroup) #origin=(-.5, .5), position=(NpcXCoor.x, NpcXCoor.y - NpcXCoor.scale_y - .04), parent=NpcGroup)
#showLines = ButtonGroup(('on', 'off'), min_selection=1, y=-.1, default='off', selected_color=color.red)

app.run()