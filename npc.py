from ursina import *
import math

class Tank(Button):
    def __init__(self, name, x=0, y=1.5, z=0, texture='tex_1.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=(x, y, z),
            model='npc/tank/tank',
            texture='npc/tank/' + texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )
        self.name = name
        self.isSelected = True

        self.vel = .1
        self.max_s = .12
        self.max_r_s = self.max_s / -2
        self.x_speed = 0
        self.z_speed = 0
        self.speed = math.sqrt(self.x_speed**2+self.z_speed**2)
        self.rot_s = 180 # in degree
        self.rotation_y = 0
        self.friction = 1/5

    def update(self):
        if self.isSelected:
            if held_keys['w'] and self.speed <= self.max_s: self.speed += self.vel * time.dt   
            if held_keys['w'] == False and self.speed != 0:
                self.speed -= self.speed/self.friction * time.dt
                if self.speed < .01:
                    self.speed = 0
            if held_keys['space']:
                self.y += 2
            self.rotation_y -= self.rot_s * time.dt * (held_keys['a'] - held_keys['d'])

        self.rotation_y %= 360
        if self.rotation_y < 0: self.rotation_y += 360
        self.position += self.back * self.speed
        
        origin = self.world_position - (0, .5, 0) # tankin zemininden hesaplicak
        hit_info = raycast(origin , self.down, ignore=(self,), debug=False)
        
        if hit_info.distance > .1:
            self.fall()

        if self.position.y <= -15:
            destroy(self)
    
    def fall(self):
        self.y -= .01
