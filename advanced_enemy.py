from ship import Ship 
import pygame
from bullet import Bullet
import settings
import os


class AdvancedEnemy(Ship):
    def __init__(self,x,y,health=200):
        super().__init__(x,y,health)
        self.ship_img , self.bullet_img = settings.ADVANCED_ENEMY_SHIP,settings.ADVANCED_ENEMY_BULLET
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self,velocity):
        self.x -= velocity
    def shoot(self):
        if self.recharge_counter == 0:
            bullet = Bullet(self.x,self.y + 20 ,self.bullet_img)
            self.bullets.append(bullet)
            self.recharge_counter = 1
    def move_bullets(self,velocity,obj):
        self.recharge()
        for bullet in self.bullets:
            bullet.move(velocity)
            if bullet.off_screen(settings.WIDTH):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 20
                self.bullets.remove(bullet)