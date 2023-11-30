import pygame

class Ground:
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        self.x = x
        self.y = y 
        self.imgpath = str(imgpath)
        self.surface = surface
        self.image = pygame.image.load(self.imgpath)
    def drawGround(self):
        self.surface.blit(self.image, (self.x, self.y))