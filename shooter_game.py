#Создай собственный Шутер!

from pygame import *
from random import randint
import time as timer
init()
windows = display.set_mode((700,500))
display.set_caption('Шутер')
clock = time.Clock()
font2 = font.SysFont('Arial', 50)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y)).convert_alpha()
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.mask = mask.from_surface(self.image)

    def reset(self):
        windows.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > -2:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx - 10,self.rect.top,5,20,20)
        bullets.add(bullet)   

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        global text_lose
        if self.rect.y > 500:
            self.rect.x = randint(0,650)
            self.rect.y = 0
            lost += 1
            text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
             
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 10:
            self.kill()

class Asteroids(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(0, 650)
            self.rect.y = 0


player = Player('rocket.png',20,400,5,70,90)
enemy1 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
enemy2 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
enemy3 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
enemy4 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
enemy5 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
asteroid1 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)
asteroid2 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)
asteroid3 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)

ufos = sprite.Group()
ufos.add(enemy1)
ufos.add(enemy2)
ufos.add(enemy3)
ufos.add(enemy4)
ufos.add(enemy5)

bullets = sprite.Group()

asteroids = sprite.Group()
asteroids.add(asteroid1)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
lifes = 3

win = font2.render('ТЫ ПОБЕДИЛ!', True, (255, 215 ,0))
game_over = font2.render('ТЫ  ПРОИГРАЛ!', True, (255, 0, 0))
life = font2.render(str(lifes), True, (255, 255, 255))


lost = 0
count = 0
font1 = font.SysFont('Arial', 26)
text_count = font1.render('Счёт: ' + str(count), 1, (255,255,255))
text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))

galaxy = transform.scale(image.load('galaxy.jpg'), (700, 500))
finish = False

#Музыка
mixer.music.load('space.ogg')
mixer.music.set_volume(0.10)
mixer.music.play()
sleep_fire = timer.time()

num_fire = 0
rel_time = False
reloads = font1.render('Wait, reload', 1, (255, 255, 255))

game = True
while game:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_r]:
        if finish != False:
            ufos.empty()
            asteroids.empty()
            bullets.empty()
            lost = 0
            count = 0
            num_fire = 0
            lifes = 3
            enemy1 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            enemy2 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            enemy3 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            enemy4 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            enemy5 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            asteroid1 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)
            asteroid2 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)
            asteroid3 = Asteroids('asteroid.png',randint(0,650),0,randint(1, 5),70,65)
            ufos.add(enemy1)
            ufos.add(enemy2)
            ufos.add(enemy3)
            ufos.add(enemy4)
            ufos.add(enemy5)
            asteroids.add(asteroid1)
            asteroids.add(asteroid2)
            asteroids.add(asteroid3)
            life = font2.render(str(lifes), True, (255, 255, 255))
            text_count = font1.render('Счёт: ' + str(count), 1, (255,255,255))
            text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
            finish = False

    if finish != True:
        if keys_pressed[K_SPACE]:
            if num_fire < 5 and rel_time == False:
                if timer.time() - sleep_fire >= 1:
                    player.fire()
                    num_fire += 1
                    sleep_fire = timer.time()
            if num_fire >= 5 and rel_time == False:
                rel_time = True
                countdown = timer.time()          
        windows.blit(galaxy,(0, 0))
        windows.blit(text_lose,(5, 5))
        windows.blit(text_count,(5, 30))
        windows.blit(life, (660,5))
        bullets.draw(windows)
        if count >= 10:
            windows.blit(win, (220, 200))
            finish = True
        if lost >= 300:
            finish = True
            windows.blit(game_over, (220, 200))
        if lifes < 1:
            finish = True
            windows.blit(game_over, (220, 200))    
        player.reset()
        player.update()
        ufos.draw(windows)
        ufos.update()
        bullets.update()
        asteroids.draw(windows)
        asteroids.update()
        collides = sprite.groupcollide(ufos, bullets, True, True, sprite.collide_mask)
        sprite_collide = sprite.spritecollide(player, ufos, True, sprite.collide_mask)
        sprite_collides = sprite.spritecollide(player, asteroids, True, sprite.collide_mask)
        for collide in collides:
            count += 1
            enemy1 = Enemy('ufo.png',randint(0,650),0,randint(1, 5),70,65)
            ufos.add(enemy1)
            text_count = font1.render('Счёт: ' + str(count), 1, (255,255,255))
        if len(sprite_collide) != 0:
            lifes -= 1
            life = font2.render(str(lifes), True, (255, 255, 255))
        if len(sprite_collides) != 0:
            lifes -= 1
            life = font2.render(str(lifes), True, (255, 255, 255))
        if rel_time == True:
            timera = timer.time()
            if timera - countdown <= 2:
                windows.blit(reloads, (270, 470))
            else:
                num_fire = 0
                rel_time = False    
                    
    for e in event.get():
        if e.type == QUIT:
            game = False    

    clock.tick(60)       
    display.update()



    