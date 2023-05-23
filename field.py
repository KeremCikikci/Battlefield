from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
fps = True
sen = 0.2

app = Ursina()

x_pos, y_pos, z_pos = 15, 12, -12
x_angle, y_angle, z_angle = 33, -33, 0 #yukari assa, saga sola,
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)
camera.orthografic = True
window.fps_counter.enabled = True
window.exit_button.visible = True
window.borderless = False

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


class Tank(Button):
    def __init__(self, position=(1, 1, 0), texture='npcs/tank/tank_tex6.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='npcs/tank/tank',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
        )
        self.vel = .1
        self.max_s = .12
        self.x_speed = 0
        self.z_speed = 0
        self.speed = math.sqrt(self.x_speed**2+self.z_speed**2)
        self.rot_s = 180 # in degree
        self.angle = 0
        self.friction = 1/5

# v = a * t
# s = 1/2 * a * t**2

    def update(self):
        if held_keys['w'] and self.speed <= self.max_s:
            self.speed += self.vel * time.dt
        if held_keys['w'] == False and self.speed != 0:
            self.speed -= self.speed/self.a * time.dt
            if self.speed < .01:
                self.speed = 0
        if held_keys['a']:
            self.angle -= (self.rot_s * time.dt)
        if held_keys['d']:
            self.angle += (self.rot_s * time.dt)

        self.angle = self.angle % 360
        if self.angle < 0:
            self.angle = 360 + self.angle

        if self.angle < 90:
            self.x_speed = -sin(math.radians(self.angle)) * self.speed
            self.z_speed = -cos(math.radians(self.angle)) * self.speed
        if self.angle >= 90 and self.angle < 180:
            self.z_speed = sin(math.radians(self.angle - 90)) * self.speed
            self.x_speed = -cos(math.radians(self.angle - 90)) * self.speed
        if self.angle >= 180 and self.angle < 270:
            self.x_speed = sin(math.radians(self.angle - 180)) * self.speed
            self.z_speed = cos(math.radians(self.angle - 180)) * self.speed
        if self.angle >= 270 and self.angle < 360:
            self.z_speed = -sin(math.radians(self.angle - 270)) * self.speed
            self.x_speed = cos(math.radians(self.angle - 270)) * self.speed
        
        self.x += self.x_speed
        self.z += self.z_speed

        self.rotation_y = self.angle
        print(self.speed)

        #self.rotation_y += 1
        #self.x += self.vel


tank2=Tank()

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

app.run()