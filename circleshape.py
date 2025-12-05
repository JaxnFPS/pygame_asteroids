import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self,other):
        result = False
        c1_pos = self.position
        c2_pos = other.position
        c1_rad = self.radius
        c2_rad = other.radius
        distance = c1_pos.distance_to(c2_pos)
        if distance <= c1_rad+c2_rad:
            result = True
        return result
