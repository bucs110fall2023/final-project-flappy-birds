import pygame 

class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        self.imgpath = imgpath
        image = pygame.image.load(self.imgpath)
        og_width, og_height = image.get_size()
        
        self.image = pygame.transform.scale(image, (og_width/3, og_height/3))
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y 
        self.surface = surface
   
    def drawPipe(self):
        self.surface.blit(self.image, (self.x, self.y))