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

class LaserBullets(BulletsClass):
    def __init__(self, type, pos, foe):
        super(LaserBullets, self).__init__(type, pos)
        self.foe = foe

    def move(self):
        self.x = self.foe.rect.centerx
        self.y += self.speed[1]
        self.rect.centerx = self.x
        self.rect.centery = self.y

class XDeviationBullets(BulletsClass):
    def __init__(self, type, pos, deviation):
        super(XDeviationBullets, self).__init__(type, pos)
        self.deviation = deviation
    def move(self):
        self.speed[0] = self.speed[0] + self.deviation
        self.speed[1] = self.speed[1] + self.deviation
        super(XDeviationBullets, self).move()

class CurveBullets(BulletsClass):
    def __init__(self, type, pos, angle):
        super(CurveBullets, self).__init__(type, pos)
        self.angle = angle

    def move(self):
        self.angle = self.angle + 1
        self.speed = Speed(self.angle)
        super(CurveBullets, self).move()

class OwnBullet1(BulletsClass):
    def __init__(self, pos, speed):
        super(OwnBullet1, self).__init__(21,pos)
        self.speed = speed
        self.atr = 10    

class OwnBullet2(BulletsClass):
    def __init__(self, pos, speed):
        super(OwnBullet2, self).__init__(22,pos)
        self.speed = speed
        self.atr = 5

#-----------------------------敌机弹幕----------------------------------
class Shoot1():
    def shooting(self, pos, epos, bullets, foe = None):
        #s = math.sqrt((epos[0] - pos[0])**2 + (epos[1] - pos[1])**2) / 12
        ang = Angle(pos, epos)
        sp = Speed(ang)
        bullet = BulletsClass(1, pos)
        bullet.speed = sp
        bullets.append(bullet)

class Shoot2():
    def shooting(self, pos, epos, bullets, foe = None):
        for i in range(18):
            ang = Angle(pos, epos)
            sp = Speed(ang + i*20)
            bullet = BulletsClass(9, pos)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot3():
    def shooting(self, pos, epos, bullets, foe = None):
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
    def shooting(self, pos, epos, bullets, foe = None):
        ang = Angle(pos, epos)
        sp = Speed(ang, 3)
        bullet = BulletsClass(18, pos)
        bullet.speed = sp
        bullets.append(bullet)

class Shoot5():
    def shooting(self, pos, epos, bullets, foe = None):
        ang = Angle(pos, epos)
        for i in range(3):
            sp = Speed(ang+(i-1)*15)
            bullet = BulletsClass(9, pos)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot6():
    def shooting(self, pos, epos, bullets, foe = None):
        bullet = LaserBullets(12, [pos[0], pos[1]+10], foe)
        bullet.speed = [0,15]
        bullets.append(bullet)

class Shoot7():
    def shooting(self, pos, epos, bullets, foe = None):
        for i in range(18):
            sp = Speed(i*20)
            bullet = XDeviationBullets(8, pos, 0.1)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot8():
    def shooting(self, pos, epos, bullets, foe = None):
        for i in range(18):
            ang = i * 20
            sp = Speed(ang)
            bullet = CurveBullets(7, pos, ang)
            bullet.speed = sp
            bullets.append(bullet)

class ShootMode():
    shoots = [Shoot1(),Shoot2(),Shoot3(),Shoot4(),Shoot5(),Shoot6(),Shoot7(),Shoot8()]
    
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
        if self.index < 3:
            self.index += 1
    def barDown(self):
        self.index = 0

class BarrageOne():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet2([pos[0], pos[1]-10], [0,-18])
        ownBullets.append(b1)

class BarrageTwo():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet2([pos[0]-13, pos[1]-10], [0,-18])
        b2 = OwnBullet2([pos[0]+13, pos[1]-10], [0,-18])
        ownBullets.append(b1)
        ownBullets.append(b2)

class BarrageThree():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet1([pos[0], pos[1]-10], [0, -18])
        sp1 = Speed(270 - 5, 18)
        #270是自机上方的角度，+ - 5为偏转角度， 18为子弹的速度参数
        b2 = OwnBullet2([pos[0], pos[1]-10], sp1)
        sp2 = Speed(270 + 5, 18)
        b3 = OwnBullet2([pos[0], pos[1]-10], sp2)
        ownBullets.append(b1)
        ownBullets.append(b2)
        ownBullets.append(b3)

class BarrageFour():
    def shooting(self, pos, ownBullets):
        b1 = OwnBullet1([pos[0], pos[1]-10], [0, -18])
        sp1 = Speed(270 - 5, 18)
        #270是自机上方的角度，+ - 5为偏转角度， 18为子弹的速度参数
        b2 = OwnBullet1([pos[0], pos[1]-10], sp1)
        sp2 = Speed(270 + 5, 18)
        b3 = OwnBullet1([pos[0], pos[1]-10], sp2)
        sp3 = Speed(270 - 10, 18)
        b4 = OwnBullet2([pos[0], pos[1]-10], sp3)
        sp4 = Speed(270 + 10, 18)
        b5 = OwnBullet2([pos[0], pos[1]-10], sp4)
        ownBullets.append(b1)
        ownBullets.append(b2)
        ownBullets.append(b3)
        ownBullets.append(b4)
        ownBullets.append(b5)
            
def angle(pos, epos):
    x = epos[0] - pos[0]
    y = epos[1] - pos[1]
    c = math.sqrt(x**2 + y**2)
    sina = y / c
    angle = math.asin(sina) * 180 / math.pi
    if x < 0:
        return (180 - angle)
    else:
        return angle

def speed(angle):
    x = 6 * math.cos(angle * math.pi/180)
    y = 6 * math.sin(angle * math.pi/180)
    speed = [x, y]
    return speed

