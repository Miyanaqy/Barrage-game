import pygame, sys, math, random

class OwnFly(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location

class BulletClass(pygame.sprite.Sprite):
    def __init__(self,image_file,pos,epos, speed = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        '''x = random.randint(-4,4)
        y = random.randint(-4,4)
        self.speed = [x, y]'''
        s = math.sqrt(mox(abs(epos[0]-pos[0])) + mox(abs(epos[1]-pos[1])))/8
        self.speed = speed
        self.speed = [(epos[0]-pos[0]) / s, (epos[1]-pos[1]) / s]
    def move(self):
        self.rect = self.rect.move(self.speed)


def mox(x):
    return x * x

def anim(bullets, own):
    global score
    for bullet in bullets:
        bullet.move()
        screen.blit(bullet.image, bullet.rect)
        if bullet.rect.centerx > 450 or bullet.rect.centery >700 or bullet.rect.centerx <0 or bullet.rect.centery < 0 :
            bullets.remove(bullet)
        if math.sqrt(mox(abs(bullet.rect.centerx-own.rect.centerx)) + mox(abs(bullet.rect.centery-own.rect.centery))) < 15 :
            score += 1
            bullets.remove(bullet)

def fonts(text, size, x, y):
    font = pygame.font.Font(None, size)
    content = font.render(text, 1,(0,0,0))
    textpos = [x, y]
    screen.blit(content, textpos)
    return content

pygame.init()
screen = pygame.display.set_mode([450,700])
screen.fill([255,255,255])
own = OwnFly('image/own.png',[250,350])
pygame.key.set_repeat(12,12)
bullets = pygame.sprite.Group()
clock = pygame.time.Clock()
global score
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                own.rect.centery -= 4
            if event.key == pygame.K_DOWN:
                own.rect.centery += 4
            if event.key == pygame.K_LEFT:
                own.rect.centerx -= 4
            if event.key == pygame.K_RIGHT:
                own.rect.centerx += 4
    clock.tick(50)
    screen.fill([255,255,255])
    b = random.randint(0,2)
    if b  == 1:
        intx = random.randint(0,450)
        inty = random.randint(0,700)
        bullet = BulletClass('image/Bullet1.png',[intx,inty], own.rect)
        bullets.add(bullet)

    screen.blit(own.image, own.rect)
    anim(bullets, own)
    fonts('on: %s' % score,16,30,30)
    pygame.display.flip()

