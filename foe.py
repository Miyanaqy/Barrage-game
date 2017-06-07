import pygame,math
from BulletsClass import *
from Rqueue import *
from drop import *
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
        self.drop.rect.center = self.rect.center
        drops.append(self.drop)

class FoeMove1():
    def __init__(self, foe, shoot):
        self.foe = foe
        self.index = 0
        self.shoot = ShootMode.get_shoot(shoot)

    def move(self, own, bullets):
        self.index += 1
        self.foe.rect.centery += 0
        if self.index % 5 == 0:
            self.shoot.shooting(self.foe.rect.center, own.rect.center, bullets)
        
			
    def coll(self):
        self.foe.coll()
