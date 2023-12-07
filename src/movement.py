import pygame

class Movement:
    def __init__(self, x , y, img = None, t=0):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.x = x
        self.y = y
        self.image = img
        self.t = t
    def pipeMove(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        pipe_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - pipe_shift
        return self.x
    
    def backgroundMove(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        screen_width = self.image.get_size()[0]
        back_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - back_shift
        
        if abs(self.x) > screen_width:
            self.x = screen_width - 10 
        return self.x
    
    def birdJump(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.y = self.y -(25*self.t)+ ((1/2) * (80) * ((self.t) ** 2))
        return self.y
    
    def birdFall(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.y = self.y + 10
        return self.y
    
    def birdSpeed(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        self.speed = -25+ (80*self.t)
        return self.speed

    def groundMove(self):
        """
        general function description
        args: (type) description
        return: (type) description
        """
        image_width = self.image.get_size()[0]
        ground_shift = (pygame.display.get_window_size()[0])/250
        self.x = self.x - ground_shift
        
        if abs(self.x) > image_width:
            self.x = image_width 
        return self.x
