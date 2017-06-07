import pygame
from Angle import *
from collision import *
class Drop():
    def __init__(self, type, pos):
        self.images = ['image/Drop/D.png','image/Drop/P2.png']
        self.image = pygame.image.load(self.images[type])
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width
        self.rect.height = self.rect.height
        self.rect.center = pos
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.speed = [0, 4]
    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.center = [self.x, self.y]

    def coll(self, drops, own):
        ang = Angle(self.rect.center, own.rect.center)
        self.speed = Speed(ang, 9)
        dis = distance(self.rect.center, own.rect.center)
        if dis < 5 :
            drops.remove(self)
            self.die(own)
        
        
class UpgradeDrop(Drop):
    def __init__(self, pos):
        super(UpgradeDrop, self).__init__(0, pos)

    def die(self, own):
        pass


class FractionDrop(Drop):
    def __init__(self, pos):
        super(FractionDrop, self).__init__(1, pos)

    def die(self, own):
        own.barrage.barUp()
        
        
