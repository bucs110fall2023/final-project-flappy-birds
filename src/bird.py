import pygame 

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def jump(self, self.x, self.y):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    jump_up = True
                else:
                    fall_down = True
                    
        