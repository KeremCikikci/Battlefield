from ursina import *
import math

sinDiff=[sin, cos, sin, cos]
cosDiff=[cos, sin, cos, sin]

class Tank(Button):
    def __init__(self, position=(1, 1, 0), texture='npc/tank/tank_tex6.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='npc/tank/tank',
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
        
        self.grounded = False
        self.gravity = True
        self.air_time = 0
        self.height = 1
        
        self.traverse_target = scene # collide with everything

        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, traverse_target=self.traverse_target)
            if ray.hit:
                self.y = ray.world_point.y

    def update(self):
        if held_keys['w'] and self.speed <= self.max_s: self.speed += self.vel * time.dt      
        if held_keys['w'] == False and self.speed != 0:
            self.speed -= self.speed/self.friction * time.dt
            if self.speed < .01:
                self.speed = 0
        self.rotation_y -= self.rot_s * time.dt * held_keys['a']
        self.rotation_y += self.rot_s * time.dt * held_keys['d']

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

        if self.gravity:
            # gravity
            ray = raycast(self.world_position, self.down, traverse_target=self.traverse_target)
            #ray = boxcast(self.world_position, self.down)
            if ray.distance <= .1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .3 and ray.world_point.y - self.world_y < .2: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 50
            self.air_time += time.dt * .25 * self.gravity

    def start_fall(self):
        self.y_animator.pause()

    def land(self):
        # print('land')
        self.air_time = 0
        self.grounded = True