import pygame 

class Pipe:
    def __init__(self, surface, x, y, imgpath):
        self.x = x
        self.y = y 
        self.imgpath = str(imgpath)
        self.surface = surface
        
    def drawPipe(self):
        image = pygame.image.load(self.imgpath)
        self.surface.blit(image, (self.x, self.y))