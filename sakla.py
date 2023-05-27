
sinDiff=[sin, cos, sin, cos]
cosDiff=[cos, sin, cos, sin]

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

        for i in range(4):
            if self.rotation_y >= i * 90 and self.rotation_y < (i+1) * 90:
                x_sign = -1 if i < 2 else 1
                z_sign = -1 if i == 0 or i == 3 else 1
                self.x_speed = sinDiff[i](math.radians(self.rotation_y - i * 90)) * x_sign
                self.z_speed = cosDiff[i](math.radians(self.rotation_y - i * 90)) * z_sign
  
        self.x += self.x_speed * self.speed
        self.z += self.z_speed * self.speed