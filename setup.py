import pygame
from math import sin, cos, radians, inf, hypot
from random import random, randint, choice

def Tuple(item = None):
    return tuple

def List(item = None):
    return list

pygame.init()
pygame.font.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
TITLE_FONT = pygame.font.Font("font.ttf", 140)
DEFAULT_FONT = pygame.font.Font("font.ttf", 100)
SMALL_FONT = pygame.font.Font("font.ttf", 60)
TINY_FONT = pygame.font.Font("font.ttf", 30)

game_volume = None

with open("data.txt", "r") as f:
    game_volume = float(f.read().split()[1])

GAME_MUSIC = pygame.mixer.Sound("audio/music.mp3")
GAME_MUSIC.set_volume(game_volume)

GAME_OVER_SOUND = pygame.mixer.Sound("audio/game_over.wav")
GAME_OVER_SOUND.set_volume(game_volume)

EXPLOSION_SOUND = pygame.mixer.Sound("audio/explosion.mp3")
EXPLOSION_SOUND.set_volume(game_volume * 2)

SELECT_SOUND = pygame.mixer.Sound("audio/select.mp3")
SELECT_SOUND.set_volume(game_volume)
