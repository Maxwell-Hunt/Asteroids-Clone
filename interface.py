from setup import *
from asteroid import Asteroid
from interface_elements import TickList

class Splash:

    def __init__(self, play_music = True):
        self.title_text = "Asteroids"
        self.instruction_text = "Press Space To Play"
        self.options_instructions = "Press O For Options"
        self.asteroids = [Asteroid(SCREEN_WIDTH * random(), SCREEN_HEIGHT * random(), Asteroid.largest_radius) for _ in range(15)]
        if play_music:
            GAME_MUSIC.play(-1)

    def update(self, delta_time : float) -> int:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            SELECT_SOUND.play()
            return 1
        elif pressed[pygame.K_o]:
            SELECT_SOUND.play()
            return 2
        for asteroid in self.asteroids:
            asteroid.update(delta_time)

    def draw(self, screen : pygame.Surface):
        title_surface = TITLE_FONT.render(self.title_text, True, (255, 255, 255))
        screen.blit(title_surface, (SCREEN_WIDTH/2 - title_surface.get_width()/2, SCREEN_HEIGHT*0.25))

        if pygame.time.get_ticks()//500 % 2 == 0:
            text_surface = SMALL_FONT.render(self.instruction_text, True, (255, 255, 255))
            screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT*0.8))

        text_surface = TINY_FONT.render(self.options_instructions, True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT*0.7))

        for asteroid in self.asteroids:
            asteroid.draw(screen)

class Options:

    x_offset = 200

    def __init__(self):
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.difficulty_selector = TickList(150, 250, self.difficulties)
    
    def update(self, delta_time : float) -> int:
        self.difficulty_selector.update(delta_time)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            SELECT_SOUND.play()
            return self.difficulty_selector.selected

    def draw(self, screen : pygame.Surface):
        subtitle1 = SMALL_FONT.render("Difficulty", True, (255, 255, 255))
        screen.blit(subtitle1, (self.x_offset - subtitle1.get_width()/2, SCREEN_HEIGHT*0.15))
        self.difficulty_selector.draw(screen)

        instruction = TINY_FONT.render("Press ESC To Exit", True, (255, 255, 255))
        screen.blit(instruction, ((SCREEN_WIDTH - instruction.get_width()) / 2, SCREEN_HEIGHT * 0.9))



class GameOver:

    duration_time = 4

    def __init__(self, score):
        self.creation_time = pygame.time.get_ticks()
        self.score = score
        self.high_score = score
        GAME_MUSIC.stop()
        GAME_OVER_SOUND.play()

        with open("data.txt", "r") as f:
            hs = int(f.read().split()[0])
            if hs > self.high_score:
                self.high_score = hs
        with open("data.txt", "w") as f:
            f.write(f"{self.high_score} {game_volume}")


    def update(self, delta_time : float) -> int:
        if pygame.time.get_ticks() - self.creation_time > self.duration_time * 1000:
            return 1

    def draw(self, screen : pygame.Surface):
        first_line = DEFAULT_FONT.render("You Destroyed", True, (255, 255, 255))
        second_line = DEFAULT_FONT.render(f"{self.score} Asteroids!", True, (255, 255, 255))
        screen.blit(first_line, (SCREEN_WIDTH/2 - first_line.get_width()/2, SCREEN_HEIGHT*0.25))
        screen.blit(second_line, (SCREEN_WIDTH/2 - second_line.get_width()/2, SCREEN_HEIGHT*0.35))

        third_line = SMALL_FONT.render(f"HIGH SCORE: {self.high_score}", True, (255, 255, 255))
        screen.blit(third_line, (SCREEN_WIDTH/2 - third_line.get_width()/2, SCREEN_HEIGHT*0.5))

