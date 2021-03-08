from setup import *

class Entity:
    
    colour = (255, 255, 255)

    def __init__(self, position_x : float, position_y : float):
        self.position = pygame.Vector2(position_x, position_y)
        self.rotation = 30

    def get_transformed_points(self) -> tuple:
        transformed_points = []
        for point in self.points:
            new_x = point.x * cos(radians(self.rotation)) - point.y * sin(radians(self.rotation))
            new_y = point.x * sin(radians(self.rotation)) + point.y * cos(radians(self.rotation))
            new_x += self.position.x
            new_y += self.position.y
            transformed_points.append((new_x, new_y))
        return tuple(transformed_points)

    def get_bounds(self) -> tuple:
        top = inf
        left = inf
        right = -inf
        bottom = -inf
        for point in self.get_transformed_points():
            right = max(point[0], right)
            bottom = max(point[1], bottom)
            left = min(point[0], left)
            top = min(point[1], top)
        return (top, right, bottom, left)

    def update(self, delta_time):
        pass

    def draw(self, screen : pygame.Surface):
        transformed_points = self.get_transformed_points()
        pygame.draw.polygon(screen, self.colour, transformed_points, 3)


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
        if pressed[pygame.K_RIGHT]:
            self.rotation += 0.5 * delta_time
        if pressed[pygame.K_LEFT]:
            self.rotation -= 0.5 * delta_time

    def screen_wrap(self):
        top, right, bottom, left = self.get_bounds()
        if left > SCREEN_WIDTH:
            self.position.x = -right + self.position.x
        if top > SCREEN_HEIGHT:
            self.position.y = -bottom + self.position.y
        if right < 0:
            self.position.x = SCREEN_WIDTH + self.position.x - left
        if bottom < 0:
            self.position.y = SCREEN_HEIGHT + self.position.y - top


    def update(self, delta_time : float):
        self.move(delta_time)
        if self.velocity.magnitude() > self.max_speed:
            self.velocity = self.velocity.normalize()
            self.velocity *= self.max_speed

        self.position += self.velocity * delta_time
        self.screen_wrap()