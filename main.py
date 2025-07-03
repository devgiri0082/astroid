import pygame
from constants import ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, ASTEROID_SPAWN_RATE, SCREEN_WIDTH
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(color=(0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quiting")
                return
        


if __name__ == "__main__":
    main()
