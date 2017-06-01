import pygame
from Rqueue import *

class OwnClass():
    def __init__(self,pos):
        self.images = []
        self.left_images = []
        self.right_images = []
        self.angle = 0
        self.speed = [0,0]
        for i in range(7):
            self.left_images.append('image/own/own_left%s.png' % (i+1))
            self.right_images.append('image/own/own_right%s.png' % (i+1))
            if i < 4:
                self.images.append('image/own/own%s.png' % (i+1))
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.imagesum = 0
        self.speed = [0, 0]

    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]
        self.imagesum += 1
        self.image = pygame.image.load(self.images[int((self.imagesum%12))//3])

    def die(self):
        rq = Rqueue.creatRq()
        images = []
        pos = self.rect
        rq.add(images,pos,len(images))
