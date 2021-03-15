from setup import *
from player import Player
from asteroid import Asteroid

class Game:

    def __init__(self, number_asteroids):
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroids = [Asteroid(SCREEN_WIDTH * choice([0, 1]), SCREEN_HEIGHT * choice([0, 1]), Asteroid.largest_radius) for _ in range(number_asteroids)]
        self.score = 0
        self.number_asteroids = number_asteroids

    def update(self, delta_time : float) -> int:

        if random() < Asteroid.spawn_chance * 0.01 or len(self.asteroids) < self.number_asteroids:
            self.asteroids.append(Asteroid(SCREEN_WIDTH * choice([0, 1]), SCREEN_HEIGHT * choice([0, 1]), Asteroid.largest_radius))

        self.player.update(delta_time)
        for asteroid in self.asteroids:
            if self.player.check_collision(asteroid):
                return 1
            
            for bullet in self.player.bullets:
                if asteroid.check_collision(bullet):
                    if asteroid.radius > Asteroid.smallest_radius:
                        self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                        self.asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                    else:
                        self.score += 1
                    EXPLOSION_SOUND.play()
                    self.asteroids.remove(asteroid)
                    self.player.bullets.remove(bullet)

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