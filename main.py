import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, ASTEROID_SPAWN_RATE, SCREEN_WIDTH
from player import Player
from shot import Shot
def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    Shot.containers = (drawable, updatable, shots)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    asteroid_field = AsteroidField()
    while True:
        screen.fill(color=(0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quiting")
                return
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide_with(asteroid) == True:
                    shot.kill()
                    asteroid.split()
                    
            if player.collide_with(asteroid) == True:
                print("collision detected")
                return
        pygame.display.flip()
        dt = clock.tick(60)/1000
       


if __name__ == "__main__":
    main()
