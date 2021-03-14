import pygame
from math import sin, cos, radians, inf
from random import random, randint, choice

def Tuple(item = None):
    return tuple

def List(item = None):
    return List

pygame.init()
pygame.font.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TITLE_FONT = pygame.font.Font("font.ttf", 140)
DEFAULT_FONT = pygame.font.Font("font.ttf", 100)
SMALL_FONT = pygame.font.Font("font.ttf", 60)

game_volume = 0.2

GAME_MUSIC = pygame.mixer.Sound("music.mp3")
GAME_MUSIC.set_volume(game_volume)

GAME_OVER_SOUND = pygame.mixer.Sound("game_over.wav")
GAME_OVER_SOUND.set_volume(game_volume)

EXPLOSION_SOUND = pygame.mixer.Sound("explosion.mp3")
EXPLOSION_SOUND.set_volume(game_volume * 2)

SELECT_SOUND = pygame.mixer.Sound("select.mp3")
SELECT_SOUND.set_volume(game_volume)
