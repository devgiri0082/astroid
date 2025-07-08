import math
from typing import ForwardRef, Sequence
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_COOLDOWN, SHOT_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        print(self.cooldown)
        new_cooldown = self.cooldown  - dt
        if new_cooldown > 0:
            self.cooldown = new_cooldown
        else:
            self.cooldown = 0

        if keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_SPACE]:
            self.shot()




    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED 
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shot(self):
        if self.cooldown > 0:
            return
        self.cooldown = SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * SHOT_SPEED
        


