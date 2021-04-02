import pygame
from ship import Ship
from bullet import Bullet
import os
import settings



class BasicEnemy(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img , self.bullet_img = settings.BASIC_ENEMY_SHIP,settings.BASIC_ENEMY_BULLET 
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self,velocity):
        self.x -= velocity
    def shoot(self):
        if self.recharge_counter == 0:
            bullet = Bullet(self.x,self.y + 20 ,self.bullet_img)
            self.bullets.append(bullet)
            self.recharge_counter = 1