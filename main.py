import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables,)
    Shot.containers = (shots, updateables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        updateables.update(dt)

        for asteroid in asteroids:
            collision = asteroid.check_for_collision(player)

            if collision:
                print("Game over!")
                sys.exit()
    
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # pause the game loop until 1/60th of a second has passed
        delta_time_seconds = game_clock.tick(60)
        delta_time_ms = delta_time_seconds / 1000
        dt = delta_time_ms

if __name__ == "__main__":
    main()
