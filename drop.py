import pygame

class Drop():
    def __init__(self, type, pos):
        self.images = {'image/drop/drop1.png'}
        self.image = pygame.image.load(self.images[type])
        self.rect = self.image.get_rect()
        self.rect.center = pos
class UpgradeDrop(Drop):
    def __init__(self, pos):
        super(UpgradeDrop, self).__init__(1, pos)
        self.speed = [5,5]
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

class FractionDrop(Drop):
    def __init__(self, pos):
        super(FractionDrop, self).__init__(2, pos)
    def move(self):
        self.rect.centery -= 9

        
        
