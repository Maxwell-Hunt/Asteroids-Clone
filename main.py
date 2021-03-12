from setup import *
from player import Player
from asteroid import Asteroid

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True

previous_time = pygame.time.get_ticks()
current_time = previous_time
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroids = [Asteroid(random() * SCREEN_WIDTH, random() * SCREEN_HEIGHT, 50) for _ in range(5)]

while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time
    screen.fill((0, 0, 0))

    player.update(delta_time)
    player.draw(screen)
    for asteroid in asteroids:
        if player.check_collision(asteroid):
            player.colour = (255, 0, 0)
            break
        
        for bullet in player.bullets:
            if asteroid.check_collision(bullet):
                if asteroid.radius > 25:
                    asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                    asteroids.append(Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius / 2))
                asteroids.remove(asteroid)
                player.bullets.remove(bullet)
        
    else:
        player.colour = (255, 255, 255)

    for asteroid in asteroids:
        asteroid.update(delta_time)
        asteroid.draw(screen)

    for bullet in player.bullets:
        bullet.update(delta_time)
        bullet.draw(screen)
        if bullet.is_off_screen:
            player.bullets.remove(bullet)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()


pygame.quit()