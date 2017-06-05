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
        s = math.sqrt(abs(epos[0] - pos[0])**2 + abs(epos[1] - pos[1])**2) / 16.0
        self.speed = [(epos[0] - pos[0]) / s, (epos[1] - pos[1]) / s]

class OwnBullet1(BulletsClass):
    def __init__(self, pos, speed):
        super(OwnBullet1, self).__init__(21,pos)
        self.speed = speed
        self.atr = 3


class Barrage():
    def __init__(self):
        self.state = [BarrageOne(), BarrageTwo(), BarrageThree(), BarrageFour()]
        self.index = 0
    def shooting(self, pos, ownBullets):
        self.state[self.index].shooting(pos, ownBullets)
    def barUp(self):
        self.index += 1

class BarrageOne():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet1([pos[0], pos[1]-10], [0,-18])
        ownBullets.append(b1)

class BarrageTwo():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet1([pos[0]-13, pos[1]-10], [0,-18])
        b2 = OwnBullet1([pos[0]+13, pos[1]-10], [0,-18])
        ownBullets.append(b1)
        ownBullets.append(b2)

class BarrageThree():
    def __init__(self):
        pass
    def shooting(self):
        pass

class BarrageFour():
    def __init__(self):
        pass
    def shooting(self):
        pass
            
