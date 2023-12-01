import pygame 

class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        
        image = pygame.image.load(imgpath)
        og_width, og_height = image.get_size()
        
        self.image = pygame.transform.scale(image, (og_width/2, og_height/2))
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y 
        self.surface = surface
   
    def drawPipe(self):
        self.surface.blit(self.image, (self.x, self.y))