from setup import *
from manager import Manager

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True
previous_time = pygame.time.get_ticks()
current_time = previous_time

game_manager = Manager()

while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time

    game_manager.update(delta_time)
    game_manager.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()