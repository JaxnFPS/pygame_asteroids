import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys
from shot import Shot
def main():
    #game state (True = On)
    Game_State = True
    fps = 60
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #initialize clock object
    clock = pygame.time.Clock()
    #initialize delta time variable
    dt = 0
    #initialize player
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    #initialize asteroid field
    asteroidfield = AsteroidField()
    while Game_State:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    s.kill()
                    a.split()
        pygame.display.flip()
        dt = (clock.tick(fps))/1000
        # print(dt)

        

if __name__ == "__main__":
    main()
