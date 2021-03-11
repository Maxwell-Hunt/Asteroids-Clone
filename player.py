from setup import *
from entity import Entity
from bullet import Bullet

class Player(Entity):

    max_speed = 0.5
    points = [pygame.Vector2(20, 0), pygame.Vector2(-20, -10), pygame.Vector2(-20, 10)]
    cool_down_time = 200

    def __init__(self, position_x : float, position_y : float):
        super().__init__(position_x, position_y)
        self.velocity = pygame.Vector2(0, 0)
        self.bullets = []
        self.cool_down = 0

    def move(self, delta_time : float):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.velocity.x += cos(radians(self.rotation)) * 0.001
            self.velocity.y += sin(radians(self.rotation)) * 0.001
        else:
            self.velocity *= 0.99
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.rotation += 0.5 * delta_time
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.rotation -= 0.5 * delta_time

    def shoot(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.cool_down <= 0:
            self.bullets.append(Bullet(self.position.x, self.position.y, self.rotation))
            self.cool_down = self.cool_down_time

    def update(self, delta_time : float):
        self.move(delta_time)
        self.shoot()
        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.velocity.normalize()
            self.velocity *= self.max_speed

        if self.cool_down > 0:
            self.cool_down -= delta_time

        self.position += self.velocity * delta_time
        self.screen_wrap()