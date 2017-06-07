import pygame,math
from BulletsClass import *
from Rqueue import *
from drop import *
from Angle import *

#---------------------------怪物类----------------------------------
class Foe():
    def __init__(self, HP, images, pos):
        self.HP = HP
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.behavior = 0
        self.index = 0

    def reImage(self):
        return pygame.image.load(self.images[int(self.index / 4) % 4])

    def coll(self, atr, drops):
        self.HP -= atr
        if self.HP < 0:
            self.die(drops)
            return True
        else:
            return False

    def die(self):
        pass

class RedFoe(Foe):
    def __init__(self, pos):
        images = ['image/foe/foe2_1.png','image/foe/foe2_2.png','image/foe/foe2_3.png','image/foe/foe2_4.png']
        super(RedFoe, self).__init__(20, images, pos)


class BlueFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe1_1.png','image/foe/foe1_2.png','image/foe/foe1_3.png','image/foe/foe1_4.png']
        super(BlueFoe, self).__init__(15, images, pos)
        self.drop = drop
        
    def die(self, drops):
        #rq = Rqueue.creatRq()
        #images = []
        #pos = self.rect
        #rq.add(images,pos,len(images))
        self.drop.x = self.rect.centerx
        self.drop.y = self.rect.centery
        drops.append(self.drop)


#--------------------------------怪物的移动类----------------------------
class FoeMove():
    def __init__(self, foe, shoot):
        self.foe = foe
        self.index = 0
        self.shoot = ShootMode.get_shoot(shoot)
    def coll(self):
        self.foe.coll()

class FoeMove1(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 45:
            self.foe.rect.centerx -= 5
        elif self.index >= 45 and self.index < 225:
            sp = Speed((360 - self.index * 2), 160)
            self.foe.rect.center = [sp[0] + 225, sp[1] + 210]
            if self.index % 10 == 0:
                self.shoot.shooting(self.foe.rect.center, own.rect.center, bullets)
        elif self.index >= 225:
            self.foe.rect.centerx -= 5
        self.foe.image = pygame.image.load(self.foe.images[int((self.index%4))])
        
class FoeMove2(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 45:
            self.foe.rect.centerx += 5
        elif self.index >= 45 and self.index < 225:
            sp = Speed(self.index * 2+180, 160)
            self.foe.rect.center = [sp[0] + 225, sp[1] + 210]
            if self.index % 10 == 0:
                self.shoot.shooting(self.foe.rect.center, own.rect.center, bullets)
        elif self.index >= 225:
            self.foe.rect.centerx += 5
        self.foe.image = pygame.image.load(self.foe.images[int((self.index%4))])

class FoeMove3(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 50:
            self.foe.rect.centery += 2
        if self.index >= 50 and self.index < 500:
            if self.index % 15 == 0:
                self.shoot.shooting(self.foe.rect.center, own.rect.center, bullets)
        if self.index > 500:
            self.foe.rect.centery += 3
            if self.index % 15 == 0:
                self.shoot.shooting(self.foe.rect.center, own.rect.center, bullets)
