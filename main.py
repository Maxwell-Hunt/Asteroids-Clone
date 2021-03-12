from setup import *
from game import Game 
from interface import Splash, GameOver

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True
previous_time = pygame.time.get_ticks()
current_time = previous_time

current_interface = Splash()
while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time
    screen.fill((0, 0, 0))

    response = current_interface.update(delta_time)
    if isinstance(current_interface, Splash):
        if response == 1:
            current_interface = Game() 
    elif isinstance(current_interface, Game):
        if response == 1:
            current_interface = GameOver(current_interface.score)
    elif isinstance(current_interface, GameOver):
        if response == 1:
            current_interface = Splash()

    current_interface.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()


pygame.quit()