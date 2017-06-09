import pygame, sys, math, random
from multiprocessing import Process
import os
from Rqueue import *
from BulletsClass import *
from own import *
from foe import *
from collision import *
from drop import *
import copy

def plot_read(chapter):
    with open('plot/plot%s.txt' % chapter) as plot_file:
        plots = plot_file.readlines()
    return plots
    
def plot_process(plots, foes):
    global proc
    global plotIndex
    proc += 1
    print(proc)
    print(len(plots),plotIndex)
    while(plotIndex < len(plots)):
        param = plots[plotIndex].split(',')
        if proc == int(param[0]):
            print(param)
            creatFoe(param, foes)
            plotIndex += 1
        else:
            return

def creatFoe(param, foes):
    shoot = ShootMode.get_shoot(int(param[1]))
    pos = [int(param[4]), int(param[5])]
    drop = get_drop(int(param[3]))
    foe = get_foe(int(param[2]), pos, drop)
    foeMove = get_foeMove(int(param[6]), foe)
    foeMove.shoot = shoot
    foes.append(foeMove)
    
#---------------------------物体移动--------------------------------
def moveAll(own, foes, bullets, ownBullets, drops):
    own.move()
    for foe in foes:
        foe.move(own, bullets)
        #敌机超出屏幕外50px后，消除敌机
        if abs(foe.foe.rect.centerx - width/2) > width/2+50 or abs(foe.foe.rect.centery - height/2) > height/2+50:
            foes.remove(foe)
    for bullet in bullets:
        bullet.move()
        #弹幕超出屏幕外100px后，消除弹幕
        if abs(bullet.rect.centerx - width/2) > width/2+100 or abs(bullet.rect.centery - height/2) > height/2+100:
            bullets.remove(bullet)
    for obullet in ownBullets:
        obullet.move()
        #自机弹幕超出屏幕10px后，消除弹幕
        if abs(obullet.rect.centerx - width/2) > width/2+10 or abs(obullet.rect.centery - height/2) > height/2+10:
            ownBullets.remove(obullet)
    for drop in drops:
        drop.move()
        #掉落物超出屏幕外12px后，消除掉落物
        if abs(drop.rect.centerx - width/2) > width/2+10 or abs(drop.rect.centery - height/2) > height/2+10:
            drops.remove(drop)
    colli1(own, foes, bullets, drops)
    colli2(foes, ownBullets)

#---------------------------物体碰撞------------------------------------
def colli1(own, foes, bullets, drops):
    global ownDie
    global dieTime
    for foe in foes:
        if collision(own, foe.foe, -10):
            die = foe.foe.coll(own.atr, drops)
            own.die()
            ownDie = True
            ownShadow.rect.center = [225,730]#初始化位置
            dieTime = 0
            if die: foes.remove(foe)
    for bullet in bullets:
        if collision(own, bullet, -10):
            bullets.remove(bullet)
            own.die()
            ownDie = True
            ownShadow.rect.center = [225,730]
            dieTime = 0
    for drop in drops:
        if collision(own, drop, 30):
            #drops.remove(drop)
            #own.barrage.barUp()
            drop.coll(drops, own)

def colli2(foes, ownBullets):
    for foe in foes:
        for bullet in ownBullets:
            if collision(foe.foe, bullet):
                die = foe.foe.coll(bullet.atr, drops)
                if die: foes.remove(foe)
                bullet.die(ownBullets)

def draw(own, foes, bullets, ownBullets, drop):
    screen.blit(own.image, own.rect)
    for foe in foes:
        screen.blit(foe.foe.image, foe.foe.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    for ownBullet in ownBullets:
        screen.blit(ownBullet.image, ownBullet.rect)
    for drop in drops:
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
global width
global height
width, height = (450,700)
screen = pygame.display.set_mode([width,height])
screen.fill([255,255,255])
global plotIndex
plotIndex = 1
bullets = []
foes = []
ownBullets = []
drops = []
own = OwnClass([250,550], width/2, height/2, ownBullets)
ownShadow = OwnShadow()
rq = Rqueue.creatRq()
pygame.key.set_repeat(12,12)
clock = pygame.time.Clock()
global score
global ownDie
plots = plot_read(1)
ownDie = False
score = 0
maxs = 0
global proc
proc = 0
global dieTime
#-------------------以下为测试内容------------------------
#-----------------掉落物drop--------------------
#drop = FractionDrop()
#-----------------弹幕类型-----------------------
#shoot = 7
#------------------怪物移动方式FoeMove,怪物外观BlueFoe-------------------
#foe = FoeMove3(BlueFoe([150,-10],drop), shoot)
#------------------怪物组foes-------------------------
#foes.append(foe)

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
                own.state = 4
            if event.key == pygame.K_RIGHT and own.rect.centerx+10<450:
                own.speed[0] = 6
                own.state = 8
            if event.key == pygame.K_z:
                own.shooting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and own.rect.centery-10>0:
                own.speed[1] = 0
            if event.key == pygame.K_DOWN and own.rect.centery+10<700 :
                own.speed[1] = 0
            if event.key == pygame.K_LEFT and own.rect.centerx-10>0:
                own.speed[0] = 0
                own.state = 0
            if event.key == pygame.K_RIGHT and own.rect.centerx+10<450:
                own.speed[0] = 0
                own.state = 0
            if event.key == pygame.K_z:
                own.shooting = False
                    


    clock.tick(50)
    plot_process(plots, foes)
    screen.fill([255,255,255])
    b = random.randint(0,20)
    moveAll(own, foes, bullets, ownBullets,drops)
    draw(own,foes,bullets,ownBullets,drops)
    if ownDie:
        dieTime += 1
        ownShadow.move()
        screen.blit(ownShadow.image, ownShadow.rect)
        if dieTime > 30:
            own.rect.center = ownShadow.rect.center
            ownDie = False
    pygame.display.flip()
    

