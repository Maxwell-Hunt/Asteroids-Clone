from setup import *
from entity import Entity

class Bullet(Entity):

    speed = 0.6
    points = [pygame.Vector2(1, 1), pygame.Vector2(-1, 1), pygame.Vector2(1, -1), pygame.Vector2(-1, -1)]

    def __init__(self, position_x : float, position_y : float, rotation : float):
        super().__init__(position_x, position_y)
        self.rotation = rotation

    def update(self, delta_time : float):
        velocity = pygame.Vector2(cos(radians(self.rotation)), sin(radians(self.rotation))).normalize() * self.speed
        self.position += velocity * delta_time
