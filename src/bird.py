import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        self.x = x
        self.y = y 
        self.imgpath = str(imgpath)
        self.surface = surface
        
        image = pygame.image.load(self.imgpath)        
        self.image = pygame.transform.scale(image, (80, 80))
        
    def drawBird(self):
        self.surface.blit(self.image, (self.x, self.y))
        