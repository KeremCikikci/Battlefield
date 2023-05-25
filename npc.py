from ursina import *
import math

sinDiff=[sin, cos, sin, cos]
cosDiff=[cos, sin, cos, sin]

class Tank(Button):
    def __init__(self, name, position=(1, 10, 0), texture='tex_1.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='npc/tank/tank',
            texture='npc/tank/' + texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            origin_y=-.5
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
        if self.isSelected:
            if held_keys['w'] and self.speed <= self.max_s: self.speed += self.vel * time.dt   

            if held_keys['w'] == False and self.speed != 0:
                self.speed -= self.speed/self.friction * time.dt
                if self.speed < .01:
                    self.speed = 0
                
            self.rotation_y -= self.rot_s * time.dt * (held_keys['a'] - held_keys['d'])

        self.rotation_y %= 360
        if self.rotation_y < 0: self.rotation_y += 360
        self.position += self.back * self.speed

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

        # collide in x-y-Plane


    def start_fall(self):
        self.y_animator.pause()

    def land(self):
        self.air_time = 0
        self.grounded = True