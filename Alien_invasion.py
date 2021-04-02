import pygame
import os
import random
import settings
from ship import Ship
from bullet import Bullet 
from basic_enemy import BasicEnemy
from main_player import Player
from advanced_enemy import AdvancedEnemy
from game_functions import collide
from game_functions import main
from game_functions import main_menu


#initialize Pygame fonts module
pygame.font.init()
WIN = settings.WIN
#window Title
pygame.display.set_caption("Space Invaders")
#Loading the Background Image...
BG = settings.BG

main_menu()