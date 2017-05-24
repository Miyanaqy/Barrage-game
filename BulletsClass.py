import pygame, math
class BulletsClass():
    def __init__(self,type,pos):
        self.type = type
        self.image = pygame.image.load('image/bullet/bullet%s.png' % type)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        self.rect = self.rect.move(self.speed)

class FoeBullets(BulletsClass):
    def __init__(self, type, pos, epos):
        super(FoeBullets, self).__init__(type,pos)
        s = math.sqrt(abs(epos[0] - pos[0])**2 + abs(epos[1] - pos[1])**2) / 8.0
        self.speed = [(epos[0] - pos[0]) / s, (epos[1] - pos[1]) / s]


class OwnBullets(BulletsClass):
    def __init__(self, type, pos):
        super(OwnBullets, self).__init__(type,pos)
        self.speed = [0,-18]
