import pygame
from pygame import mixer
import os

#window width and height
WIDTH = 750
HEIGHT = 700
#displaying the window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#enemy bullets speed
enemy_bullet_velocity = 3
#player bullets speed
player_bullet_velocity = 4
#enemy speed
enemy_moving_speed = 1
# player moving speed
moving_speed = 3

#fonts used  ...
pygame.font.init()
lost_font = pygame.font.SysFont("Sans Serif",80)
main_font = pygame.font.SysFont("Sans Serif",40)

#text color in RGB format ...
black_rgb =(0,0,0)
white_rgb =(255,255,255)

#Images ...

#Loading the Background Image...
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
#Loading the main player space ship...
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("assets", "player_ship.png"))
#Loading main player bullets ...
PLAYER_BULLET = pygame.image.load(os.path.join("assets","player_bullet.png"))
#Loading basic enemy space ship ...
BASIC_ENEMY_SHIP =pygame.image.load(os.path.join("assets", "basic_enemy.png"))
#Loading basic enemy bullet ...
BASIC_ENEMY_BULLET = pygame.image.load(os.path.join("assets", "basic_enemy_bullet.png"))
#Loading advanced enemy space ship ...
ADVANCED_ENEMY_SHIP =pygame.image.load(os.path.join("assets", "advanced_enemy.png"))
#Loading advanced enemy bullet ...
ADVANCED_ENEMY_BULLET = pygame.image.load(os.path.join("assets", "advanced_enemy_bullet.png"))

# SOUND FX...
pygame.mixer.init()
#Loading the background music
background_music = os.path.join("assets","space.mp3")
#Loading player bullet sound
bullet_sound_path = os.path.join("assets","pew.wav")
bullet_sound =mixer.Sound(bullet_sound_path)
#Loading ditroy Sound FX
distroy_sound_path = os.path.join("assets","distroy.ogg")
distroy_sound = mixer.Sound(distroy_sound_path)