from setup import *
from entity import Entity
from asteroid import Asteroid

class Player(Entity):

    max_speed = 0.5
    points = [pygame.Vector2(20, 0), pygame.Vector2(-20, -10), pygame.Vector2(-20, 10)]

    def __init__(self, position_x : float, position_y : float):
        super().__init__(position_x, position_y)
        self.velocity = pygame.Vector2(0, 0)

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

    def check_collision(self, asteroids : List(Asteroid)) -> bool:
        points = self.get_transformed_points()
        for asteroid in asteroids:
            asteroid_points = asteroid.get_transformed_points()
            axes = []
            for vertices in (points, asteroid_points):
                for i in range(len(vertices)):
                    point1 = pygame.Vector2(vertices[i][0], vertices[i][1])
                    point2 = pygame.Vector2(vertices[i-1][0], vertices[i-1][1])

                    edge = point2 - point1
                    normal = pygame.Vector2(-edge.y, edge.x).normalize()
                    axes.append(normal)

            for axis in axes:
                self_max = -inf
                self_min = inf
                asteroid_max = -inf
                asteroid_min = inf
                for point in points:
                    p = axis.dot(point)
                    self_max = max(p, self_max)
                    self_min = min(p, self_min)
                for point in asteroid_points:
                    p = axis.dot(point)
                    asteroid_max = max(p, asteroid_max)
                    asteroid_min = min(p, asteroid_min)

                if not (self_max > asteroid_min and self_min < asteroid_max):
                    break
            else:
                return True
                
        return False

    def update(self, delta_time : float):
        self.move(delta_time)
        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.velocity.normalize()
            self.velocity *= self.max_speed

        self.position += self.velocity * delta_time
        self.screen_wrap()