from ursina import *
app = Ursina()
descr = dedent('''
  Rainstorm
  Summon a rain storm to deal 5 water

  damage to everyone, test including yourself.
  1234 1234 1234 1234 1234 1234 2134 1234 1234 1234 1234 1234 2134 2134 1234 1234 1234 1234
  Lasts for 4 rounds.''').strip()

Text.default_resolution = 1080 * Text.size
test = Text(text=descr, wordwrap=30)




def input(key):
  if key == 'a':
      print('a')
      test.text = '<default><image:file_icon> <red><image:file_icon> test '
      print('by', test.text)

window.fps_counter.enabled = False
print('....', Text.get_width('yolo'))
app.run()