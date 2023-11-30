import pygame

class Movement:
    def __init__(self, x , y, img):
        self.x = x
        self.y = y
        self.image = img
    def pipeMove(self):
        pipe_shift = (pygame.display.get_window_size()[0])/20
        self.x = self.x - pipe_shift
        return self.x
    
    def backgroundMove(self):
        screen_width = self.image.get_size()[0]
        back_shift = (pygame.display.get_window_size()[0])/150
        self.x = self.x - back_shift
        
        if abs(self.x) > screen_width:
            self.x = screen_width - 10 
        return self.x
    
    def birdMove(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.y = self.y - (300 * 1.718) + ((1000 * ((1.718) ** 2))/2)
            else:
                self.y = self.y + ((1000 * ((1.718) ** 2))/2)
    
    def groundMove(self):
        image_width = self.image.get_size()[0]
        ground_shift = (pygame.display.get_window_size()[0])/150
        self.x = self.x - ground_shift
        
        if abs(self.x) > image_width:
            self.x = image_width - 10 
        return self.x
