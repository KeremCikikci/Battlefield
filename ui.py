from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

def renderUI(cam):
    Panel = Entity(model='quad', origin=(-.5, .5), position=(.5, .5), scale=(.4, 1), color=color.dark_gray, parent=camera.ui)

    CamGroup = Button(model='quad', origin=(-.5, .5), position=(.05, -.05), scale=(.4, .03), text="Camera", text_color=color.dark_gray, color=color.azure, parent=Panel)

    CamCoorGroup = Entity(model='quad', origin=(-.5, .5), position=(CamGroup.x, CamGroup.y - CamGroup.scale_y), scale=(.87, .05), color=color.azure, parent=Panel)

    CamXCoor = InputField(model='quad', text='x: ' + str(cam[0]), character_limit=6, max_lines=1, origin=(-.5, .5), position=(.05, -.3), scale_x=.25, scale_y=.5, parent=CamCoorGroup)
    CamYCoor = InputField(model='quad', text='y: ' + str(cam[1]), character_limit=6, max_lines=1, origin=(-.5, .5), position=(CamXCoor.x + CamXCoor.scale_x + .05, CamXCoor.y), scale_x=CamXCoor.scale_x, scale_y=CamXCoor.scale_y, parent=CamCoorGroup)
    CamZCoor = InputField(model='quad', text='z: ' + str(cam[2]), character_limit=6, max_lines=1, origin=(-.5, .5), position=(CamYCoor.x + CamYCoor.scale_x + .05, CamYCoor.y), scale_x=CamYCoor.scale_x, scale_y=CamYCoor.scale_y, parent=CamCoorGroup)

    Selector = DropdownMenu('select', text_origin=(-1.05, 1.6), model='quad', origin=(-.5, .5), position=(CamCoorGroup.x, CamCoorGroup.y - CamCoorGroup.scale_y - .02), scale=(CamCoorGroup.scale_x, .04), color=color.azure, parent=Panel, 
                            buttons=(DropdownMenuButton('New', color=color.light_gray),))

    NpcGroup = Entity(model='quad', origin=(-.5, .5), position=(Selector.x, Selector.y - Selector.scale_y - .01), scale=(Selector.scale_x, .3), color=color.azure, parent=Panel)

    NpcXCoor = InputField(model='quad', text='x:', character_limit=6, max_lines=1, origin=(-.5, .5), position=(CamXCoor.x, -.05), scale_x=.25, scale_y=.1, parent=NpcGroup)
    NpcYCoor = InputField(model='quad', text='y:', character_limit=6, max_lines=1, origin=(-.5, .5), position=(NpcXCoor.x + NpcXCoor.scale_x + .05, NpcXCoor.y), scale_x=NpcXCoor.scale_x, scale_y=NpcXCoor.scale_y, parent=NpcGroup)
    NpcZCoor = InputField(model='quad', text='z:', character_limit=6, max_lines=1, origin=(-.5, .5), position=(NpcYCoor.x + NpcYCoor.scale_x + .05, NpcYCoor.y), scale_x=NpcYCoor.scale_x, scale_y=NpcYCoor.scale_y, parent=NpcGroup)

    showLinesText = Text('Show Lines', origin=(-.5, .5), position=(NpcXCoor.x, NpcXCoor.y - NpcXCoor.scale_y - .04), scale=3, parent=NpcGroup)
    showLinesButtonGroup = ButtonGroup(('on', 'off'), origin=(-.5, .5), position=(NpcXCoor.x, showLinesText.y - .1), scale=.12, min_selection=1, default='off', selected_color=color.red, parent=NpcGroup)
