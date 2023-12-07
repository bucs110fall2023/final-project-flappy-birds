import pygame 

class Pipe(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.imgpath = imgpath
        image = pygame.image.load(self.imgpath)
        og_width, og_height = image.get_size()
        
        self.image = pygame.transform.scale(image, (og_width/3, og_height/3))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.surface = surface
        self.mask = pygame.mask.from_surface(self.image)
   
    def drawPipe(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.surface.blit(self.image, (self.rect.x, self.rect.y))