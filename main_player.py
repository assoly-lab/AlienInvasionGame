import settings
from ship import Ship
import pygame
from pygame import mixer
import os



#Loading the main player space ship...
PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("assets", "player_ship.png"))
#Loading main player bullets ...
PLAYER_BULLET = pygame.image.load(os.path.join("assets","player_bullet.png"))

#main player class ...
class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = PLAYER_SPACE_SHIP
        self.bullet_img = PLAYER_BULLET
        self.mask = pygame.mask.from_surface(PLAYER_SPACE_SHIP)
        self.max_health = health
    #fonction to move bullets and handle collisions with enemies    
    def move_bullets(self,velocity,objs):
        self.recharge()
        for bullet in self.bullets:
            bullet.move(velocity)
            if bullet.off_screen(settings.WIDTH):
                self.bullets.remove(bullet)
            else :
                for obj in objs:
                    if bullet.collision(obj):
                        mixer.Sound.play(settings.distroy_sound)
                        obj.health -= 100
                        self.bullets.remove(bullet)
                    if obj.health <=0 :
                        objs.remove(obj)
   #fonction to draw health bar                     
    def draw(self,window):
        super().draw(window)
        self.health_bar(window)
    #fonction to handle player health (if got hit lower down health ...)
    def health_bar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x  - 10, self.y + 10  , 5, self.ship_img.get_width()))
        if self.health <= 0:
            pygame.draw.rect(window, (0,255,0), (self.x  - 10, self.y + 10 , 5, 0))
        else :
            pygame.draw.rect(window, (0,255,0), (self.x  - 10, self.y + 10 , 5, self.ship_img.get_width() * (self.health/self.max_health)))
