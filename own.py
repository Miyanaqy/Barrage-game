import pygame

class OwnClass():
    def __init__(self,poi):
        self.images = []
        self.left_images = []
        self.right_images = []
        self.angle = 0
        for i in range(7):
            self.left_images.append('image/own/own_left%s.png' % (i+1))
            self.right_images.append('image/own/own_right%s.png' % (i+1))
            if i < 4:
                self.images.append('image/own/own%s.png' % (i+1))
        self.image = pygame.image.load(self.images[0])
        self.rect = self.image.get_rect()
        self.rect.center = poi
        self.imagesum = 0

    def left(self):
        if self.angle < 3:
            self.angle += 1
        else:
            self.imagesum += 1
            if self.imagesum > 3: self.imagesum = 0
        self.image = pygame.image.load(self.left_images[self.angle+self.imagesum])
        return self.image
    def right(self):
        if self.angle < 3:
            self.angle += 1
        else:
            self.imagesum += 1
            if self.imagesum > 3: self.imagesum = 0
        self.image = pygame.image.load(self.right_images[self.angle+self.imagesum])
        return self.image
    def imagees(self):
        self.imagesum += 1
        if self.imagesum > 3: self.imagesum = 0
        self.image = pygame.image.load(self.images[self.imagesum])
        return self.image