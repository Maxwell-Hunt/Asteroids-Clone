from setup import *
from entity import Entity

class Asteroid(Entity):

    speed = 0.25
    radius_variation = 0.2
    spawn_chance = 0.005
    largest_radius = 50
    smallest_radius = 25

    def __init__(self, position_x : float, position_y : float, radius : float):
        super().__init__(position_x, position_y)
        self.velocity = pygame.Vector2(random() * 2 - 1, random() * 2 - 1).normalize() * self.speed
        self.num_sides = 12
        self.radius = radius
        self.points = []
        for i in range(self.num_sides):
            angle = i * (360 / self.num_sides)
            rv = random() * self.radius_variation * 2 - self.radius_variation
            self.points.append(pygame.Vector2(cos(radians(angle)), sin(radians(angle))) * radius * (1 + rv))
            
    def update(self, delta_time : float):
        self.position += self.velocity * delta_time
        self.screen_wrap()