import pygame,math
from BulletsClass import *
from Rqueue import *
from drop import *
from Angle import *

#---------------------------怪物类----------------------------------
class Foe():
    def __init__(self, HP, images, pos, drop):
        self.HP = HP
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.drop = drop

    def coll(self, atr, drops):
        self.HP -= atr
        if self.HP < 0:
            self.die(drops)
            return True
        else:
            return False

    def die(self, drops):
        self.drop.x = self.rect.centerx
        self.drop.y = self.rect.centery
        drops.append(self.drop)

class PinkFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe2_1.png','image/foe/foe2_2.png','image/foe/foe2_3.png','image/foe/foe2_4.png']
        super(PinkFoe, self).__init__(10, images, pos, drop)

class BlueFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe1_1.png','image/foe/foe1_2.png','image/foe/foe1_3.png','image/foe/foe1_4.png']
        super(BlueFoe, self).__init__(15, images, pos, drop)

class VioletFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe3_1.png','image/foe/foe3_2.png','image/foe/foe3_3.png','image/foe/foe3_4.png']
        super(VioletFoe, self).__init__(30, images, pos, drop)

class RedFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe4_1.png','image/foe/foe4_2.png','image/foe/foe4_3.png','image/foe/foe4_4.png']
        super(RedFoe, self).__init__(60, images, pos, drop)
    
class OrangeFoe(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/foe5_1.png','image/foe/foe5_2.png','image/foe/foe5_3.png','image/foe/foe5_4.png']
        super(OrangeFoe, self).__init__(150, images, pos, drop)

class ssBoss(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/ssBoss_1.png','image/foe/ssBoss_2.png']
        super(ssBoss, self).__init__(400, images, pos, drop)

class sBoss1(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/sBoss1_1.png','image/foe/sBoss1_2.png','image/foe/sBoss1_3.png','image/foe/sBoss1_4.png']
        super(sBoss1, self).__init__(1000, images, pos, drop)

class sBoss2(Foe):
    def __init__(self, pos, drop):
        images = ['image/foe/sBoss2_1.png','image/foe/sBoss2_2.png','image/foe/sBoss2_3.png','image/foe/sBoss2_4.png']
        super(sBoss2, self).__init__(1000, images, pos, drop)
        

def get_foe(index, pos, drop):
    if index == 0:
        foe = PinkFoe(pos, drop)
    elif index == 1:
        foe = BlueFoe(pos, drop)
    elif index == 2:
        foe = VioletFoe(pos, drop)
    elif index == 3:
        foe = RedFoe(pos, drop)
    elif index == 4:
        foe = OrangeFoe(pos, drop)
    elif index == 5:
        foe = ssBoss(pos, drop)
    elif index == 11:
        foe = sBoss1(pos, drop)
    elif index == 12:
        foe = sBoss2(pos, drop)
    return foe

#--------------------------------怪物的移动类----------------------------
class FoeMove():
    def __init__(self, foe):
        self.foe = foe
        self.index = 0
        if self.foe.rect.centerx > 225:
            self.direction = -1
        else:
            self.direction = 1
    def coll(self, atr, drops, foes):
        if self.foe.coll(atr, drops):
            try:
                foes.remove(self)
            except ValueError as e:
                print(e)

class FoeMove1(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 45:
            self.foe.rect.centerx -= 5
        elif self.index >= 45 and self.index < 225:
            sp = Speed((360 - self.index * 2), 160)
            self.foe.rect.center = [sp[0] + 225, sp[1] + 210]
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        elif self.index >= 225:
            self.foe.rect.centerx -= 5
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])
        
class FoeMove2(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 45:
            self.foe.rect.centerx += 5
        elif self.index >= 45 and self.index < 225:
            sp = Speed(self.index * 2+180, 160)
            self.foe.rect.center = [sp[0] + 225, sp[1] + 210]
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        elif self.index >= 225:
            self.foe.rect.centerx += 5 * self.direction
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove3(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 50:
            self.foe.rect.centery += 2
        if self.index >= 50 and self.index < 500:
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        if self.index > 500:
            self.foe.rect.centery += 3
            if self.index % 15 == 0:
                self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove4(FoeMove):
    def move (self, own, bullets):
        self.index += 1
        if self.index < 50:
            self.foe.rect.centery += 2
        elif self.index == 50:
            self.cen = self.foe.rect.centerx
        elif self.index > 50 and self.index < 500:
            x = 80 * math.sin((self.index-50) * math.pi/180)
            self.foe.rect.centerx = self.cen + x * self.direction
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets, self.foe)
        elif self.index == 500:
            ang = Angle(self.foe.rect.center, own.rect.center)
            sp = Speed(ang)
            self.speed = sp
        elif self.index > 500:
            self.foe.rect.centery += self.speed[0]
            self.foe.rect.centerx += self.speed[1]
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove5(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 50:
            self.foe.rect.centerx += 2 *self.direction
            self.foe.rect.centery += 2
        elif self.index >= 50 and self.index <= 500:
            if self.index % 50 == 0:
                self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        elif self.index >500:
            self.foe.rect.centerx -= 2 * self.direction
            self.foe.rect.centery += 2
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove6(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 50:
            self.foe.rect.centery += 2
        elif self.index == 50:
            ang = (self.foe.rect.center, own.rect.center)
            sp = (ang, 8)
        elif self.index > 50:
            self.foe.rect.centerx += sp[0]
            self.foe.rect.centery += sp[1]
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove7(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        self.foe.rect.centery -= 2
        self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove8(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index == 1:
            self.x = 6
            self.y = 4
        if self.index < 70:
            self.x = self.x * 0.9
            self.y = self.y * 0.9
            self.foe.rect.centerx += self.x
            self.foe.rect.centery += self.y
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        else:
            self.x = self.x * 1.1
            self.y = self.y * 1.1
            self.foe.rect.centerx += self.x
            self.foe.rect.centery += self.y
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets)
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%8) / 2))])

class FoeMove11(FoeMove):
    def move(self, own, bullets):
        self.index += 1
        if self.index < 40:
            self.foe.rect.centery += 2
        elif self.index >= 40:
            self.shoot.shooting(self.index, self.foe.rect.center, own.rect.center, bullets, self.foe)
        self.foe.image = pygame.image.load(self.foe.images[int(((self.index%2) / 2))])

class BossMove0(FoeMove):
    def move(self, own, bullets):
        self.foe.rect.centery += 3
        if self.foe.rect.centery > 50:
            return True
    def replaceMove(self):
        return BossMove2(self.foe)


class BossMove1(FoeMove):
    def move(self, own, bullets):
        pass
    def replaceMove(self): 
        return BossMove2(self.foe)

    
class BossMove2(FoeMove):
    def move(self, own, bullets):
        pass
    def replaceMove(self):
        return BossMove3(self.foe)

class BossMove3(FoeMove):
    def move(self, own, bullets):
        pass
    def replaceMove(self):
        return BossMove4(self.foe)

class BossMove4(FoeMove):
    def move(self, own, bullets):
        pass

def get_foeMove(index, foe):
    if index == 0:
        foeMove = FoeMove1(foe)
    elif index == 1:
        foeMove = FoeMove2(foe)
    elif index == 2:
        foeMove = FoeMove3(foe)
    elif index == 3:
        foeMove = FoeMove4(foe)
    elif index == 4:
        foeMove = FoeMove5(foe)
    elif index == 5:
        foeMove = FoeMove6(foe)
    elif index == 6:
        foeMove = FoeMove7(foe)
    elif index == 7:
        foeMove = FoeMove8(foe)
    elif index ==10:
        foeMove = FoeMove11(foe)
    
    return foeMove
