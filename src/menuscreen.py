import pygame

class MenuScreen:
    def __init__(self, surface, x, y):
        self.x = x
        self.y = y 
        self.surface = surface
    
    def build_menu(self):
        pygame.draw.rect(self.surface