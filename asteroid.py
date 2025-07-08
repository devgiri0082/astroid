from random import uniform
import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, width=2, radius=self.radius, center=self.position, color="white")

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius) 
        ast1.velocity = vel1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius) 
        ast2.velocity = vel2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt

