from setup import *
from game import Game 
from interface import Splash, GameOver, Options

class Manager:

    def __init__(self):
        self.current_interface = Splash()
        self.number_asteroids = 5

    def adjust_volume(self):
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


    def update(self, delta_time : float):
        self.adjust_volume()
        response = self.current_interface.update(delta_time)

        if isinstance(self.current_interface, Splash):
            if response == 1:
                self.current_interface = Game(self.number_asteroids) 
            elif response == 2:
                self.current_interface = Options()

        elif isinstance(self.current_interface, Game):
            if response == 1:
                self.current_interface = GameOver(self.current_interface.score)

        elif isinstance(self.current_interface, GameOver):
            if response == 1:
                self.current_interface = Splash()
                
        elif isinstance(self.current_interface, Options):
            if response != None:
                if response == 0:
                    self.number_asteroids = 5
                elif response == 1:
                    self.number_asteroids = 10
                elif response == 2:
                    self.number_asteroids = 15
                self.current_interface = Splash(play_music = False)
        

    def draw(self, screen : pygame.Surface):
        screen.fill((0, 0, 0))
        self.current_interface.draw(screen)