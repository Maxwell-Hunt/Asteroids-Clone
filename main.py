from setup import *
from entity import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True

previous_time = pygame.time.get_ticks()
current_time = previous_time
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time
    screen.fill((0, 0, 0))

    player.update(delta_time)
    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()


pygame.quit()