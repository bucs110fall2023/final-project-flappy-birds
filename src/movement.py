import pygame

class Movement:
    def __init__(self, x , y, img = None, t=0):
        self.x = x
        self.y = y
        self.image = img
        self.t = t
    def pipeMove(self):
        pipe_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - pipe_shift
        return self.x
    
    def backgroundMove(self):
        screen_width = self.image.get_size()[0]
        back_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - back_shift
        
        if abs(self.x) > screen_width:
            self.x = screen_width - 10 
        return self.x
    
    def birdJump(self):
        self.y = self.y -(25*self.t)+ ((1/2) * (80) * ((self.t) ** 2))
        return self.y
    
    def birdFall(self):
        self.y = self.y + 5
        return self.y
    
    def birdSpeed(self):
        self.speed = -25+ (80*self.t)
        return self.speed

    def groundMove(self):
        image_width = self.image.get_size()[0]
        ground_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - ground_shift
        
        if abs(self.x) > image_width:
            self.x = image_width 
        return self.x
