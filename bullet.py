import pygame

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class Bullet:
    def __init__(self,x,y,image):
        self.x = x 
        self.y = y 
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self,window):
        window.blit(self.image,(self.x ,self.y ))
    def move(self,vilocity):
        self.x -= vilocity
    def off_screen(self, width):
        return self.x <= 0 and width >= 750
    def collision(self,obj):
        return collide(self,obj)