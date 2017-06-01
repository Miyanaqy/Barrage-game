import pygame, sys, math, random
from multiprocessing import Process
import os
from Rqueue import *
from BulletsClass import *
from own import OwnClass
from foe import *
from collision import *
from Drop import *

def moveAll(own, foes, bullets, ownBullets, drop):
    own.move()
    for foe in foes:
        foe.move()
    for bullet in bullets:
        bullet.move()
    for obullet in ownBullets:
        obullet.move()

    drop.move()

def colli1(own, foes, bullets,drops):
    for foe in foes:
        if collision(own, foe):
            foe.coll(own,drops)
    for bullet in bullets:
        if collision(own, bullet):
            pass

def colli2(foes, ownBullets):
    for foe in foes:
        for bullet in ownBullets:
            if collision(foe, bullet):
                pass

def draw(own, foes, bullets, ownBullets, drop):
    screen.blit(own.image, own.rect)
    for foe in foes:
        screen.blit(foe.image, foe.rect)
    for bullet in bullets:
        screen.blit(bullet,image, bullet.rect)
    for ownBullet in ownBullets:
        screen.blit(ownBullet.image, ownBullet.rect)

    screen.blit(drop.image, drop.rect)

def rqueueDraw(rq):
    rq.add(None,None,True,0)
    draw = rq.head
    while draw:
        screen.blit(draw.image[draw.number-1], draw.pos)
        draw.loop()
        draw = draw.next
        if draw.bool:
            break

pygame.init()
screen = pygame.display.set_mode([450,700])
screen.fill([255,255,255])
own = OwnClass([250,550])
rq = Rqueue.creatRq()
pygame.key.set_repeat(12,12)
bullets = []
foes = []
ownBullets = []
drops = []
clock = pygame.time.Clock()
global score
score = 0
maxs = 0
drop = FractionDrop([250,30])
drops.append(drop)
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

        if event.type == pygame.KEYUP:
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
    moveAll(own, foes, bullets, ownBullets,drop)
    draw(own,foes,bullets,ownBullets,drop)
    pygame.display.flip()


