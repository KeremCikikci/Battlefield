from ursina import *
from ursina import ursinamath
import math
import uuid
from terrain import blocks, npcs

class Tank(Button):
    def __init__(self, name, x=0, y=1.5, z=0, texture='tex_1_green.png', origin=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=(x, y, z),
            model='npc/tank/tank',
            texture='npc/tank/' + texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin=origin
        )
        self.id = uuid.uuid1()
        self.name = name
        self.isSelected = True

        self.vel = .1
        self.max_s = .12
        self.max_r_s = self.max_s / -2
        self.x_speed = 0
        self.z_speed = 0
        self.speed = math.sqrt(self.x_speed**2+self.z_speed**2)
        self.rot_s = 180
        self.rotation_y = 0
        self.friction = 1/5

        self.max_fall_s = 1
        self.fall_s = 0
        self.gravity = 2

        self.cooldown = 1 # sn
        self.fireTime = 0

        self.enemies = []

    def update(self):
        self.fall_s = 0

        origin = self.world_position - (0, .5, 0) # tankin zemini

        if self.isSelected:
            hit_f = boxcast(self.world_position + (0, .1, 0), self.back, ignore=(self,), distance=.51, debug=False)
            hit_l = boxcast(self.world_position + (0, .1, 0), self.right, ignore=(self,), distance=.51, debug=True)
            hit_r = boxcast(self.world_position + (0, .1, 0), self.left, ignore=(self,), distance=.51, debug=False)
            
            if not hit_f and not hit_l and not hit_r:
                if held_keys['w'] and self.speed <= self.max_s: self.speed += self.vel * time.dt   
                if held_keys['w'] == False and self.speed != 0:
                    self.speed -= self.speed/self.friction * time.dt
                    if self.speed < .01:
                        self.speed = 0
            else:
                self.speed = 0
                self.position += self.forward / 10

            self.rotation_y -= self.rot_s * time.dt * (held_keys['a'] - held_keys['d'])
        
        self.rotation_y %= 360
        if self.rotation_y < 0: self.rotation_y += 360
        self.position += self.back * self.speed
        self.y -= self.fall_s
        
        hit_d = boxcast(origin + (-.5, 0, .5) , self.down, ignore=(self,), debug=False, distance= .1)

        if not hit_d:
            self.fall()

        if self.position.y <= -2:
            destroy(self)
        
        if held_keys['space'] and self.fireTime >= self.cooldown:
            self.fire()

        if self.fireTime < self.cooldown:
            self.fireTime += time.dt

    def fall(self):
        if self.fall_s < self.max_fall_s:
            self.fall_s += self.gravity * time.dt
            self.y -= self.fall_s

    def fire(self):
        self.fireTime = 0
        Bullet(self, self.position, self.rotation_y)

class Bullet(Button):
    def __init__(self, own, position, rotation_y):
        super().__init__(
            parent=scene,
            position=position,
            model='blocks/block',
            scale=.2,
            color=color.black,
            rotation_y=rotation_y        
        )
        self.id = uuid.uuid1()
        self.start_pos = position
        self.own = own
        self.speed = 200

    def update(self):
        self.position += self.back * self.speed * time.dt
        
        hit = raycast(self.world_position + (0, .1, 0), self.back, ignore=(self,), distance=1, debug=False)

        if ursinamath.distance(self.start_pos, self.position) > 100:
            destroy(self)

        if hit:
            for npc in npcs:
                if npc.id == hit.entity.id:
                    destroy(npc)
            for block in blocks:
                if block.id == hit.entity.id:
                    destroy(block)
            destroy(self)

        