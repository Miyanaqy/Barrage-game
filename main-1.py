import pygame, sys, math, random
from Rqueue import *
from BulletsClass import *
from own import OwnClass
from foe import *
from collision import *


pygame.init()
screen = pygame.display.set_mode([450,700])
screen.fill([255,255,255])
own = OwnClass([250,550])
rq = Rqueue()
pygame.key.set_repeat(12,12)
bullets = []
foes = []
ownBullets = []
clock = pygame.time.Clock()
global score
score = 0
maxs = 0

def moveAll(own, foes, bullets, ownBullets):
    own.move()
    for foe in foes:
        foe.move()
    for bullet in bullets:
        bullet.move()
    for obullet in ownBullets:
        obullet.move()

def colli1(own, foes, bullets):
    for foe in foes:
        if collision(own, foe):
            pass
    for bullet in bullets:
        if collision(own, bullet):
            pass

def colli2(foes, ownBullets):
    for foe in foes:
        for bullet in ownBullets:
            if collision(foe, bullet):
                pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and own.rect.centery-10>0:
                own.speed[1] = -6
            if event.key == pygame.K_DOWN and own.rect.centery+10<700 :
                own.speed[1] = 6
            if event.key == pygame.K_LEFT and own.rect.centerx-10>0:
                own.speed[0] = -6
            if event.key == pygame.K_RIGHT and own.rect.centerx+10<450:
                own.speed[0] = 6
            if event.key == pygame.K_z:
                own.shooting = True
        if eent.type = pygame.KEYUP:
            if event.key == pygame.K_UP and own.rect.centery-10>0:
                own.speed[1] = 0
            if event.key == pygame.K_DOWN and own.rect.centery+10<700 :
                own.speed[1] = 0
            if event.key == pygame.K_LEFT and own.rect.centerx-10>0:
                own.speed[0] = 0
            if event.key == pygame.K_RIGHT and own.rect.centerx+10<450:
                own.speed[0] = 0
            if event.key == pygame.K_z:
                own.shooting = False
                

    clock.tick(50)
    screen.fill([255,255,255])
    b = random.randint(0,20)
    anim(bullets, own,rq)
    pygame.display.flip()

