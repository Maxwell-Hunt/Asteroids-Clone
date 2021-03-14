from setup import *
from game import Game 
from interface import Splash, GameOver

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
is_running = True
previous_time = pygame.time.get_ticks()
current_time = previous_time
current_interface = Splash()

def adjust_volume():
    global game_volume
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        game_volume *= 0.99
    if pressed[pygame.K_RIGHT] and game_volume < 1:
        game_volume *= 1.01
    hs = None
    with open("data.txt", "r") as f:
        hs = int(f.read().split()[0])
    with open("data.txt", "w") as f:
        f.write(f"{hs} {game_volume}")
    GAME_MUSIC.set_volume(game_volume)
    GAME_OVER_SOUND.set_volume(game_volume)
    EXPLOSION_SOUND.set_volume(game_volume * 2)

while is_running:
    current_time = pygame.time.get_ticks()
    delta_time = current_time - previous_time
    previous_time = current_time
    screen.fill((0, 0, 0))

    adjust_volume()
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