import pygame

class Ground:
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        self.x = x
        self.y = y 
        self.imgpath = str(imgpath)
        self.surface = surface
        
        self.image = pygame.image.load(self.imgpath)
        og_height = self.image.get_size()[1]
        new_width= self.surface.get_size()[0]
        self. enlarged_image = pygame.transform.scale(self.image, (new_width, og_height))
        
    def drawGround(self):
        self.surface.blit(self.enlarged_image, (self.x, self.y))