import numpy as np
import random
import math

class Robot:
    def __init__(self, x, y, radius=5.0, speed=100):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = 0.0
        self.rotating = False
        self.rotation_timer = 0.0

    def update(self, dt):
        if self.rotating:
            self.angle += np.random.uniform(-1, 1) * dt * 3
            self.rotation_timer -= dt
            if self.rotation_timer <= 0:
                self.rotating = False
        else:
            self.x += self.speed * dt * math.cos(self.angle)
            self.y += self.speed * dt * math.sin(self.angle)

    def check_collision(self, arena):
        if self.x < 0 or self.x > arena.width or self.y < 0 or self.y > arena.height:
            self.rotating = True
            self.rotation_timer = random.uniform(0.5, 1.0)
