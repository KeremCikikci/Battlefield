from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

sinDiff=[sin, cos, sin, cos]
cosDiff=[cos, sin, cos, sin]
#-sin, -cos, sin, cos
#-cos, sin, cos, -sin
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

class Bullet(Entity):
    def __init__(self, position, model='cube', scale=0.1):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            scale=scale,
            #texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
        )

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
        self.rotation_y = 0
        self.friction = 1/5
        #self.barrel_x = self.x + self.scale_x / 2
        #self.barrel_y = self.y + self.scale_y / 2
        #self.barrel_z = 0
        #self.bullet = Bullet(position=(self.barrel_x, self.barrel_y, self.barrel_z))

    def update(self):
        if held_keys['w'] and self.speed <= self.max_s: self.speed += self.vel * time.dt      
        if held_keys['w'] == False and self.speed != 0:
            self.speed -= self.speed/self.friction * time.dt
            if self.speed < .01:
                self.speed = 0
        if held_keys['a']: self.rotation_y -= (self.rot_s * time.dt)
        if held_keys['d']: self.rotation_y += (self.rot_s * time.dt)

        self.rotation_y %= 360
        if self.rotation_y < 0: self.rotation_y += 360
        
        for i in range(4):
            if self.rotation_y >= i * 90 and self.rotation_y < (i+1)*90:
                x_sign = -1 if i < 2 else 1
                z_sign =  -1 if i == 0 or i == 3 else 1
                self.x_speed = sinDiff[i](math.radians(self.rotation_y - i * 90)) * x_sign
                self.z_speed = cosDiff[i](math.radians(self.rotation_y - i * 90)) * z_sign
  
        self.x += self.x_speed * self.speed
        self.z += self.z_speed * self.speed

tank2=Tank()

def input(key):
    pass

def update():
    pass

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