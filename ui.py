from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

app = Ursina()

window.borderless = False

Sky()

green = '708F7F'
grey  = '70808F'
white = 'D9D9D9'


class xyzKit:
    def __init__(self, margin_y, title: str, color1, color2):
        Title = Button(text=title, origin=(-.5, .5), scale=(camBox.scale_x, .02), x=Panel_.x + margin_x, y=margin_y - .01, color=color.hex(color2), text_color=color.hex(color1), disabled=True)
        xBox = Button(model='quad', origin=(-.5, .5), scale=(.03, .03), x=camBox.x + .01, y=Title.y-Title.scale_y-.01, color=color.hex(color1), text_color=color.hex(color2), text='x', disabled=True)
        xInputField = InputField(text='x', model='quad', origin=(-.5, .5), scale_x=.07, scale_y=xBox.scale_y, x=xBox.x + xBox.scale_x + .003, y=xBox.y, color=color.hex(white), text_color=color.hex(color2), character_limit=4)
        yBox = Button(model='quad', origin=(-.5, .5), scale=(.03, .03), x=xInputField.x + xInputField.scale_x + .03, y=xBox.y, color=color.hex(color1), text_color=color.hex(color2), text='y', disabled=True)
        yInputField = InputField(text='y', model='quad', origin=(-.5, .5), scale_x=.07, scale_y=yBox.scale_y, x=yBox.x + yBox.scale_x + .004, y=yBox.y, color=color.hex(white), text_color=color.hex(color2), character_limit=4)
        zBox = Button(model='quad', origin=(-.5, .5), scale=(.03, .03), x=yInputField.x + yInputField.scale_x + .03, y=yBox.y, color=color.hex(color1), text_color=color.hex(color2), text='z', disabled=True)
        zInputField = InputField(text='z', model='quad', origin=(-.5, .5), scale_x=.07, scale_y=zBox.scale_y, x=zBox.x + zBox.scale_x + .003, y=yBox.y, color=color.hex(white), text_color=color.hex(color2), character_limit=4)




##708F8E, #70808F, #708F7F, #D9D9D9
#  .............., .............., yesil, beyaz

margin_x = .025

Panel_ = Entity(model='quad', parent=camera.ui, origin=(-.5, .5), scale_x=1*window.aspect_ratio/4, y=.5, color=color.hex(green))
Panel_.x = .5 * window.aspect_ratio - Panel_.scale_x

camButton = Button(model='quad', origin=(-.5, .5), scale=(.4, .04), x=Panel_.x + margin_x, y=.45, color=color.hex(grey), text='Cameras', disabled=True)

camTitle = Button(model='quad', origin=(-.5, .5), scale=(.2, .04), x=Panel_.x + margin_x, y=camButton.y-camButton.scale_y - .02, color=color.hex(grey), text='Camera 1', disabled=True)

camBox = Button(model='quad', origin=(-.5, .5), scale=(.4, .18), x=Panel_.x + margin_x, y=camTitle.y-camTitle.scale_y, color=color.hex(grey), disabled=True)

Title = Button(text='Coordinates', origin=(-.5, .5), scale=(camBox.scale_x, .02), x=Panel_.x + margin_x, y=camBox.y - .02, color=color.hex(grey), text_color=color.hex(white), disabled=True)
xBox = Button(origin=(-.5, .5), scale=(.03, .03), x=camBox.x + .01, y=Title.y-Title.scale_y-.01, color=color.hex(white), text_color=color.hex(grey), text='x', disabled=True)
xInputField = InputField(text='x', origin=(-.5, .5), scale_x=.07, scale_y=xBox.scale_y, x=xBox.x + xBox.scale_x + .003, y=xBox.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)
yBox = Button( origin=(-.5, .5), scale=(.03, .03), x=xInputField.x + xInputField.scale_x + .03, y=xBox.y, color=color.hex(white), text_color=color.hex(grey), text='y', disabled=True)
yInputField = InputField(text='y', origin=(-.5, .5), scale_x=.07, scale_y=yBox.scale_y, x=yBox.x + yBox.scale_x + .004, y=yBox.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)
zBox = Button(origin=(-.5, .5), scale=(.03, .03), x=yInputField.x + yInputField.scale_x + .03, y=yBox.y, color=color.hex(white), text_color=color.hex(grey), text='z', disabled=True)
zInputField = InputField(text='z', origin=(-.5, .5), scale_x=.07, scale_y=zBox.scale_y, x=zBox.x + zBox.scale_x + .003, y=yBox.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)

Title2 = Button(text='Angles', origin=(-.5, .5), scale=(camBox.scale_x, .02), x=Panel_.x + margin_x, y=zInputField.y - zInputField.scale_y - .02, color=color.hex(grey), text_color=color.hex(white), disabled=True)
#xBoxAngle = Button(origin=(-.5, .5), scale=(.03, .03), x=camBox.x + .01, y=Title2.y-Title2.scale_y-.01, color=color.hex(white), text_color=color.hex(grey), text='x', disabled=True)
#xInputFieldAngle = InputField(text='x', origin=(-.5, .5), scale_x=.07, scale_y=xBoxAngle.scale_y, x=xBoxAngle.x + xBoxAngle.scale_x + .003, y=xBoxAngle.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)
#yBoxAngle = Button(origin=(-.5, .5), scale=(.03, .03), x=xInputFieldAngle.x + xInputFieldAngle.scale_x+.03, y=xBoxAngle.y, color=color.hex(white), text_color=color.hex(grey), text='y', disabled=True)
#yBoxAngle = Button(origin=(-.5, .5), scale=(.03, .03), x=xInputFieldAngle.x + xInputFieldAngle.scale_x + .03,y=xBoxAngle.y, color=color.hex(white), text_color=color.hex(grey), text='y', disabled=True)
#yInputFieldAngle = InputField(text='y', origin=(-.5, .5), scale_x=.07, scale_y=yBoxAngle.scale_y, x=yBoxAngle.x + yBoxAngle.scale_x + .004, y=yBox.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)
# zBoxAngle = Button(origin=(-.5, .5), scale=(.03, .03), x=yInputFieldAngle.x + yInputFieldAngle.scale_x + .03, y=yBoxAngle.y, color=color.hex(white), text_color=color.hex(grey), text='z', disabled=True)
# zInputFieldAngle = InputField(text='z', origin=(-.5, .5), scale_x=.07, scale_y=zBoxAngle.scale_y, x=zBoxAngle.x + zBoxAngle.scale_x + .003, y=yBox.y, color=color.hex(white), text_color=color.hex(grey), character_limit=4)

EditorCheckBox = Button(origin=(-.5, .5), scale=.04, x=camBox.x, y=camBox.y-camBox.scale_y-.02, color=color.hex(white))
EditorText = Text(text='Editor Camera', origin=(-.5, .5), x=EditorCheckBox.x + EditorCheckBox.scale_x + .012, y=EditorCheckBox.y - .01, color=color.hex(white))

npcButton = Button(model='quad', origin=(-.5, .5), scale=(.4, .04), x=Panel_.x + margin_x, y=EditorCheckBox.y - EditorCheckBox.scale_y - .04, color=color.hex(grey), text='NPCs', disabled=True)



app.run()