import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()

        self.imgpath = str(imgpath)
        self.surface = surface
        self.rise_rotation_angle = 5
        self.fall_rotation_angle = 5
        
        image = pygame.image.load(self.imgpath)    
            
        self.image = pygame.transform.scale(image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    
    def drawBird(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y)) 
    
    def drawJumpBird(self):
        self.rotated_image = pygame.transform.rotate(self.image, self.rise_rotation_angle)
        self.surface.blit(self.rotated_image, (self.rect.x, self.rect.y))
        
        
    def drawFallBird(self):
        self.rotated_image = pygame.transform.rotate(self.image, self.rise_rotation_angle)
        self.surface.blit(self.rotated_image, (self.rect.x, self.rect.y))
        