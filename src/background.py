import pygame

class Background:
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.x = x
        self.y = y
        self.imgpath = str(imgpath)
        self.surface = surface
        self.image = pygame.image.load(self.imgpath)
    def drawBackground(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.surface.blit(self.image, (self.x, self.y))
