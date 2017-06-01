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

    def coll(self, own):
        self.HP -= 100
        if HP < 0:
            self.die()
        own.die()

    def die(self):
        pass

class RedFoe(Foe):
    def __init__(self, pos):
        images = ['image/foe/foe2_1.png','image/foe/foe2_2.png','image/foe/foe2_3.png','image/foe/foe2_4.png']
        super(RedFoe, self).__init__(20, images, pos)

    def move(self):
        pass

class BlueFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe1_1.png','image/foe/foe1_2.png','image/foe/foe1_3.png','image/foe/foe1_4.png']
        super(BlueFoe, self).__init__(15, images, pos)
        self.drop = drop

    def move(self, own, bullets):
        self.index += 1
        if self.index < 70:
            self.rect.centerx -= 210/70.0
            
        elif self.index < 250:
            self.rect.centerx = 160 * math.sin((self.index+20)*2*math.pi/180)+225
            self.rect.centery = 160 * math.cos((self.index+20)*2*math.pi/180)+220
            if self.index > 80 and self.index <110 and self.index % 5 == 0 :
                bullet = FoeBullets(1,self.rect.center,own.rect.center)
                bullets.append(bullet)

        elif self.index >= 250:
            self.rect.centerx -= 4

    def die(self):
        rq = Rqueue.creatRq()
        images = []
        pos = self.rect
        
        rq.add(images,pos,len(images))
