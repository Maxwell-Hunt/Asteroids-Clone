from setup import *

class Entity:
    
    colour = (255, 255, 255)

    def __init__(self, position_x : float, position_y : float):
        self.position = pygame.Vector2(position_x, position_y)
        self.rotation = 0

    def get_transformed_points(self) -> Tuple(Tuple(float)):
        transformed_points = []
        for point in self.points:
            new_x = point.x * cos(radians(self.rotation)) - point.y * sin(radians(self.rotation))
            new_y = point.x * sin(radians(self.rotation)) + point.y * cos(radians(self.rotation))
            new_x += self.position.x
            new_y += self.position.y
            transformed_points.append((new_x, new_y))
        return tuple(transformed_points)

    def get_bounds(self) -> Tuple(float):
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
        pass

    def draw(self, screen : pygame.Surface):
        transformed_points = self.get_transformed_points()
        pygame.draw.polygon(screen, self.colour, transformed_points, 3)

    def check_collision(self, other) -> bool:
        points = self.get_transformed_points()
        other_points = other.get_transformed_points()
        axes = []
        for vertices in (points, other_points):
            for i in range(len(vertices)):
                point1 = pygame.Vector2(vertices[i][0], vertices[i][1])
                point2 = pygame.Vector2(vertices[i-1][0], vertices[i-1][1])

                edge = point2 - point1
                normal = pygame.Vector2(-edge.y, edge.x)
                axes.append(normal)

        for axis in axes:
            self_max = -inf
            self_min = inf
            other_max = -inf
            other_min = inf
            for point in points:
                p = axis.dot(point)
                self_max = max(p, self_max)
                self_min = min(p, self_min)
            for point in other_points:
                p = axis.dot(point)
                other_max = max(p, other_max)
                other_min = min(p, other_min)

            if not (self_max > other_min and self_min < other_max):
                break
        else:
            return True
                
        return False