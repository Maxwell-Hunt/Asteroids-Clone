from setup import *
from game import Game 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True
previous_time = pygame.time.get_ticks()
current_time = previous_time

ASTEROIDS = Game()

while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time
    screen.fill((0, 0, 0))

    ASTEROIDS.update(delta_time)
    ASTEROIDS.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()


pygame.quit()