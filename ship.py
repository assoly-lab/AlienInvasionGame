import settings
from bullet import Bullet




class Ship:  
    
    RECHARGING = 30
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.bullet_img = None
        self.bullets =[]
        self.recharge_counter = 0
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(window)
    def move_bullets(self,velocity,obj):
        self.recharge()
        for bullet in self.bullets:
            bullet.move(velocity)
            if bullet.off_screen(settings.WIDTH):
                self.bullets.remove(bullet)
            elif bullet.collision(obj):
                obj.health -= 10
                self.bullets.remove(bullet)
    def get_width(self):
        return self.ship_img.get_width()
    def get_height(self):
        return self.ship_img.get_height()
    def recharge(self):
        if self.recharge_counter >= self.RECHARGING:
            self.recharge_counter = 0
        elif self.recharge_counter > 0 :
            self.recharge_counter +=1
    def shoot(self):
        if self.recharge_counter == 0:
            bullet = Bullet(self.x,self.y + 52 ,self.bullet_img)
            self.bullets.append(bullet)
            self.recharge_counter = 1
