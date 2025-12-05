import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state
from player import Player
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
    Player.containers = (updatable,drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #initialize clock object
    clock = pygame.time.Clock()
    #initialize delta time variable
    dt = 0
    #initialize player
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while Game_State:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        for a in drawable:
            a.draw(screen)
        for a in updatable:
            a.update(dt)
        pygame.display.flip()
        dt = (clock.tick(fps))/1000
        # print(dt)

        

if __name__ == "__main__":
    main()
