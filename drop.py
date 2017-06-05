import pygame

class Drop():
    def __init__(self, type, pos):
        self.images = ['image/Drop/D.png','image/Drop/P2.png']
        self.image = pygame.image.load(self.images[type])
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width
        self.rect.height = self.rect.height
        self.rect.center = pos
class UpgradeDrop(Drop):
    def __init__(self, pos):
        super(UpgradeDrop, self).__init__(0, pos)
        self.speed = [5,5]
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

class FractionDrop(Drop):
    def __init__(self, pos):
        super(FractionDrop, self).__init__(1, pos)
    def move(self):
        self.rect.centery += 4

        
        
