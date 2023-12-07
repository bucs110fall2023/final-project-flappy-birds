import pygame

class Ground(pygame.sprite.Sprite):
    
    def __init__(self, surface, imgpath, x = 0 , y = 0):
        super().__init__()
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.imgpath = str(imgpath)
        self.surface = surface
        
        image = pygame.image.load(self.imgpath)
        og_height = image.get_size()[1]
        new_width= self.surface.get_size()[0]
        self.image = pygame.transform.scale(image, (new_width, og_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        
    def drawGround(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.surface.blit(self.image, (self.rect.x, self.rect.y))