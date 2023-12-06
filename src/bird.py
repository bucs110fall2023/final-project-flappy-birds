import pygame 

class Bird(pygame.sprite.Sprite):
    def __init__(self, surface, imgpath, x, y):
        super().__init__()

        self.imgpath = str(imgpath)
        self.surface = surface
        self.rotation_angle = 0

        
        image = pygame.image.load(self.imgpath)
        image_width, image_height = image.get_size()    
            
        self.image = pygame.transform.scale(image, (image_width/10, image_height/10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.mask = pygame.mask.from_surface(self.image)
    
    def drawBird(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y)) 
    
    def drawJumpBird(self):
        self.rotated_image = pygame.transform.rotate(self.image, self.rotation_angle)
        self.surface.blit(self.rotated_image, (self.rect.x, self.rect.y))
        
        
        