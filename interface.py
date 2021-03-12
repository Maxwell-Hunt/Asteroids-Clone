from setup import *

class Splash:

    def __init__(self):
        self.title_text = "Asteroids"
        self.instruction_text = "Press Space To Play"
        GAME_MUSIC.play(-1)

    def update(self, delta_time : float) -> int:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            return 1

    def draw(self, screen : pygame.Surface):
        text_surface = TITLE_FONT.render(self.title_text, True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT*0.25))

        if pygame.time.get_ticks()//500 % 2 == 0:
            text_surface = SMALL_FONT.render(self.instruction_text, True, (255, 255, 255))
            screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT*0.8))

class GameOver:
    duration_time = 5
    def __init__(self, score):
        self.creation_time = pygame.time.get_ticks()
        self.score = score
        self.high_score = score
        GAME_MUSIC.stop()
        GAME_OVER_SOUND.play()

        with open("highscore.txt", "r") as f:
            hs = int(f.read())
            if hs > self.high_score:
                self.high_score = hs
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))


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

