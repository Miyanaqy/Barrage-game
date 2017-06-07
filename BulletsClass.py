import pygame, math
from Angle import *
import random

#----------------------------子弹类-------------------------------------
class BulletsClass():
    def __init__(self,type,pos):
        self.type = type
        self.image = pygame.image.load('image/bullet/bullet%s.png' % type)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def die(self, ownBullets):
        ownBullets.remove(self)

class OwnBullet1(BulletsClass):
    def __init__(self, pos, speed):
        super(OwnBullet1, self).__init__(21,pos)
        self.speed = speed
        self.atr = 3    


#-----------------------------敌机弹幕----------------------------------
class Shoot1():
    def shooting(self, pos, epos, bullets):
        #s = math.sqrt((epos[0] - pos[0])**2 + (epos[1] - pos[1])**2) / 12
        ang = Angle(pos, epos)
        sp = Speed(ang)
        bullet = BulletsClass(1, pos)
        bullet.speed = sp
        bullets.append(bullet)

class Shoot2():
    def shooting(self, pos, epos, bullets):
        for i in range(18):
            ang = i * 20
            sp = Speed(ang)
            bullet = BulletsClass(9, pos)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot3():
    def shooting(self, pos, epos, bullets):
        apos = random.randint(0, 360)
        rpos = random.randint(0, 50)
        p = Speed(apos, rpos)
        pos = [pos[0] + p[0], pos[1] + p[1]]
        ang = Angle(pos, epos)
        sp = Speed(ang)
        bullet = BulletsClass(5, pos)
        bullet.speed = sp
        bullets.append(bullet)

class Shoot4():
    def shooting(self, pos, epos, bullets):
        ang = Angle(pos, epos)
        sp = Speed(ang, 3)
        bullet = BulletsClass(18, pos)
        bullet.speed = sp
        bullets.append(bullet)

class ShootMode():
    shoots = [Shoot1(),Shoot2(),Shoot3(),Shoot4()]
    
    @classmethod
    def get_shoot(cls,shoot):
        return ShootMode.shoots[shoot]


#---------------------------自机弹幕--------------------------------------
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
            



