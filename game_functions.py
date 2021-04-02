import settings
import pygame
from pygame import mixer
from main_player import Player
import random
from advanced_enemy import AdvancedEnemy
from basic_enemy import BasicEnemy

WIN = settings.WIN



def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#main fonction controls all events of the game
def main():
    #initialize pygame mixer module
    pygame.mixer.init()
    #adding background music
    mixer.music.load(settings.background_music)
    mixer.music.play(-1)

    clock = pygame.time.Clock()
    run =True
    #frame per seconds (game speed)
    FPS=60
    # instatiating the player in position x = 10 and y = 475
    main_player = Player(10,475)
    #default level
    level = 0
    #default lives
    lives = 3
    #store enemies spots Y axis
    enemies = []
    lost = False
    lost_count = 0
    enemies_number = 0

    def Update_Window():
        WIN.blit(settings.BG,(0,0))
        # background = pygame.Surface(WIN.get_size())
        # background.fill((255, 255, 255))
        # WIN.blit(background, (0, 0))
        enemies_label = settings.main_font.render("enemies left : {}".format(len(enemies)),1,(255,255,255))
        lives_label = settings.main_font.render (f"Lives: {lives}",1,(255,255,255))
        level_label = settings.main_font.render(f"Level: {level}",1,(255,255,255))
        WIN.blit(enemies_label,(10,10))
        WIN.blit(level_label,(settings.WIDTH - level_label.get_width() - 10,10))
        WIN.blit(lives_label,(settings.WIDTH / 2,10))

        for enemy in enemies :
            enemy.draw(WIN)

        main_player.draw(WIN)
        if lost:
            lost_label = settings.lost_font.render ("You Lost !",1,(255,0,0))
            WIN.blit(lost_label,(settings.WIDTH / 2 - lost_label.get_width() / 2,settings.HEIGHT / 2 ))
        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        Update_Window()
        if lives <= 0 or main_player.health <= 0:
            lost = True
            lost_count +=1
        if lost:
            if lost_count > FPS * 4:
                run =False
            else:
                continue


        if len(enemies) == 0:
            level +=1
            if level <= 9 :
                enemies_number += 5
            elif level >=10 :
                enemies_number += 6
            
            for i in range(enemies_number):
                enemy_type=("BasicEnemy","AdvancedEnemy")
                choosen_enemy= random.choice(enemy_type)
                if choosen_enemy == "BasicEnemy": 
                    enemy = BasicEnemy(random.randrange(750,1750),random.randrange(40,settings.HEIGHT - 100))
                    enemies.append(enemy)
                elif choosen_enemy=="AdvancedEnemy":
                    enemy = AdvancedEnemy(random.randrange(750,1900),random.randrange(40,settings.HEIGHT - 100))
                    enemies.append(enemy)
     #   if red X icon is pressed ...player exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        #moving player according to key pressed...
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and main_player.x - settings.moving_speed - 13 > 0:    #moving left
            main_player.x -=settings.moving_speed
        if keys[pygame.K_RIGHT] and main_player.x + settings.moving_speed + main_player.get_width() < settings.WIDTH: #moving right
            main_player.x += settings.moving_speed
        if keys[pygame.K_UP] and main_player.y - settings.moving_speed > 0:    #moving up
            main_player.y -= settings.moving_speed
        if keys[pygame.K_DOWN] and main_player.y + settings.moving_speed + main_player.get_height()  < settings.HEIGHT:   #moving down
            main_player.y += settings.moving_speed
        if keys[pygame.K_SPACE]:
            mixer.Sound.play(settings.bullet_sound)
            main_player.shoot()
        
        for enemy in enemies[:]:
            enemy.move(settings.enemy_moving_speed)
            enemy.move_bullets(settings.enemy_bullet_velocity,main_player)
            if random.randrange(0 ,480) == 1 :
                enemy.shoot()


            if collide(enemy,main_player):
                
                main_player.health -= 10
                enemies.remove(enemy)
                
                # main_player.health -= 20
                # enemies.remove(enemy)
            
            if enemy.x + enemy.get_width() < 0 :
                lives-=1
                enemies.remove(enemy)
            
            
        main_player.move_bullets(-settings.player_bullet_velocity,enemies)

#main menu triggers main fonction when ENTER key is pressed
def main_menu():
    run = True
    while run:
        WIN.blit(settings.BG,(0,0))
        Title_label = settings.main_font.render("Press ENTER to Begin...",1,settings.white_rgb)
        WIN.blit(Title_label , (settings.WIDTH / 2 - Title_label.get_width() / 2,375))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_RETURN] :
                main()