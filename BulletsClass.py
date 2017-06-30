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

class DroopBullets(BulletsClass):
    def move(self):
        self.speed[0] = self.speed[0] * 0.99
        self.speed[1] = self.speed[1] * 1.01
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.centerx = self.x
        self.rect.centery = self.y

class DecayBullets(BulletsClass):
    def __init__(self, type, pos, time):
        super(DecayBullets, self).__init__(type, pos)
        self.time = time

    def move(self):
        self.time -= 1
        if self.time = 0:
            bu = self.next
            while bu:
                bu.time = 0
                bu.speed = (0, 4)
                bu = bu.next
        super(DecayBullets, self).move()
                

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
    def shooting(self, index, pos, epos, bullets, foe = None):
        #s = math.sqrt((epos[0] - pos[0])**2 + (epos[1] - pos[1])**2) / 12
        if index % 8 == 0:
            ang = Angle(pos, epos)
            sp = Speed(ang)
            bullet = BulletsClass(1, pos)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot2():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index %25 == 0:
            for i in range(18):
                ang = Angle(pos, epos)
                sp = Speed(ang + i*20)
                bullet = BulletsClass(9, pos)
                bullet.speed = sp
                bullets.append(bullet)

class Shoot3():
    def shooting(self,index,  pos, epos, bullets, foe = None):
        if index % 6 == 0:
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
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 40 == 0:
            ang = Angle(pos, epos)
            sp = Speed(ang, 3)
            bullet = BulletsClass(18, pos)
            bullet.speed = sp
            bullets.append(bullet)

class Shoot5():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 14 == 0:
            ang = Angle(pos, epos)
            for i in range(3):
                sp = Speed(ang+(i-1)*15)
                bullet = BulletsClass(9, pos)
                bullet.speed = sp
                bullets.append(bullet)

class Shoot6():
    def shooting(self, index, pos, epos, bullets, foe = None):
        bullet = LaserBullets(12, [pos[0], pos[1]+10], foe)
        bullet.speed = [0,15]
        bullets.append(bullet)

class Shoot7():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 25 == 0:
            for i in range(18):
                sp = Speed(i*20)
                bullet = XDeviationBullets(8, pos, 0.1)
                bullet.speed = sp
                bullets.append(bullet)

class Shoot8():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 25 == 0:
            for i in range(18):
                ang = i * 20
                sp = Speed(ang)
                bullet = CurveBullets(7, pos, ang)
                bullet.speed = sp
                bullets.append(bullet)

class Shoot9():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 15 == 0:
            x = random.randint(1,12)
            x = x - 6
            bullet = DroopBullets(11, [pos[0] + x, pos[1]])
            bullet.speed = [x, 1]
            bullets.append(bullet)
            

class ShootMode():
    shoots = [Shoot1(),Shoot2(),Shoot3(),Shoot4(),Shoot5(),Shoot6(),Shoot7(),Shoot8()]
    shoots.append(Shoot9())
    @classmethod
    def get_shoot(cls,shoot):
        return ShootMode.shoots[shoot]


#---------------------------Boss弹幕--------------------------------------

class BossShoot1():
    def shooting(self, index, pos, epos, bullets, foe = None):
        if index % 5 == 0:
            y = random.randint(0, 750)
            x = random.randint(0, 1) * 450
            if x == 0:
                sp = (2, 0)
            else:
                sp = (-2, 0)
            bullet = BulletsClass(3, [x, y])
            bullet.speed = sp
            bullets.append(bullet)

class BossShoot2():
    def shooting(self, index, pos, epos, bullets, foe = None):
        for i in range(5):
            for j in range(8):
                x = (i-2) * 30
                bullet = BulletsClass(8, [epos[0] + x, epos[1]])
                ang = Angle(pos, bullet.rect.center)
                sp = Speed(ang, (j+1)*2)
                bullet.speed = sp
                bullets.append(bullet)

class BossShoot3():
    def shooting(self, index, pos, epos, bullets, foe = None):
        time = 40
        sp = (0, 0)
        nextBu = None
        for i in range(100):
            x = random.randint(0, 450)
            y = random.randint(0, 750)
            if x > pos[0] + 40 or x < pos[0] - 40:
                if y > pos[1] + 40 or y < pos[1] - 40:
                    bullet = DecayBullets(5, [x, y], time)
                    bullet.speed = sp
                    if nextBu != None:
                        bullet.next = nextBu
                    nextBu = bullet
                    bullets.append(bullet)

class BossShoot4():
    def shooting(self, index, pos, epos, bullets, foe = None):
        pass

class BossShoot5():
    def shooting(self, index, pos, epos, bullets, foe = None):
        pass

class BossShoot6():
    def shooting(self, index, pos, epos, bullets, foe = None):
        pass

class BossShoot7():
    def shooting(self, index, pos, epos, bullets, foe = None):
        pass

class BossShoot8():
    def shooting(self, index, pos, epos, bullets, foe = None):
        pass

class BossShootMode():
    shoots = [BossShoot1(),BossShoot2(),BossShoot3(),BossShoot4(),BossShoot5(),BossShoot6(),BossShoot7(),BossShoot8()]
    @classmethod
    def get_shoot(cls,shoot):
        return BossShootMode.shoots[shoot]
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

