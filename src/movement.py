import pygame

class Movement:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    def pipeMove(self):
        pipe_shift = (pygame.display.get_window_size()[0])/20
        self.x = self.x - pipe_shift
        return self.x
    
    def backgroundMove(self):
        back_shift = (pygame.display.get_window_size()[0])/35
        self.x = self.x - back_shift
        return self.x
    
    def birdMove(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x = self.x - (300 * 1.718) + ((1000 * ((1.718) ** 2))/2)
            else:
                self.x = self.x + ((1000 * ((1.718) ** 2))/2)
    
    def groundMove(self):
        ground_shift = (pygame.display.get_window_size()[0])/20
        self.x = self.x - ground_shift
        return self.x
