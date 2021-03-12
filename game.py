from setup import *
from player import Player
from asteroid import Asteroid

class Game:

    num_asteroids = 0

    def __init__(self):
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroids = [Asteroid(random() * SCREEN_WIDTH, random() * SCREEN_HEIGHT, Asteroid.largest_radius) for _ in range(self.num_asteroids)]

    def update(self, delta_time : float):

        if random() < Asteroid.spawn_chance * 0.01:
            self.asteroids.append(Asteroid(SCREEN_WIDTH * choice([0, 1]), SCREEN_HEIGHT * choice([0, 1]), Asteroid.largest_radius))

        self.player.update(delta_time)
        for asteroid in self.asteroids:
            if self.player.check_collision(asteroid):
                self.player.colour = (255, 0, 0)
                break
            
            for bullet in self.player.bullets:
                if asteroid.check_collision(bullet):
                    if asteroid.radius > Asteroid.smallest_radius:
                        self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                        self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                    self.asteroids.remove(asteroid)
                    self.player.bullets.remove(bullet)
            
        else:
            self.player.colour = (255, 255, 255)

        for asteroid in self.asteroids:
            asteroid.update(delta_time)

        for bullet in self.player.bullets:
            bullet.update(delta_time)
            if bullet.is_off_screen:
                self.player.bullets.remove(bullet)

    def draw(self, screen : pygame.Surface):
        self.player.draw(screen)

        for asteroid in self.asteroids:
            asteroid.draw(screen)

        for bullet in self.player.bullets:
            bullet.draw(screen)