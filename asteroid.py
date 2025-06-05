import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius > ASTEROID_MIN_RADIUS:
            new_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(new_angle)
            vector2 = self.velocity.rotate(-new_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            small1 = Asteroid(self.position.x, self.position.y, new_radius)
            small2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            small1.velocity = vector1 * ASTEROID_SMALL_NEW_VEL_MULTIPLIER
            small2.velocity = vector2 * ASTEROID_SMALL_NEW_VEL_MULTIPLIER
        else:
            return
        