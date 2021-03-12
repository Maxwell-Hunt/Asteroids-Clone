from setup import *
from entity import Entity

class Bullet(Entity):

    speed = 0.6
    points = [pygame.Vector2(1, 1), pygame.Vector2(-1, -1)]

    def __init__(self, position_x : float, position_y : float, rotation : float):
        super().__init__(position_x, position_y)
        self.rotation = rotation
        self.is_off_screen = False

    def update(self, delta_time : float):
        velocity = pygame.Vector2(cos(radians(self.rotation)), sin(radians(self.rotation))).normalize() * self.speed
        self.position += velocity * delta_time
        if self.position.x > SCREEN_WIDTH or self.position.x < 0 or self.position.y > SCREEN_HEIGHT or self.position.y < 0:
            self.is_off_screen = True
