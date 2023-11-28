import pygame
from src.background import Background
from src.movement import Movement




class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        
    
    def mainloop(self):
        self.state = "MENU"
        x = 0
        while True:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state =="END":
                self.endloop()
                

            

    def menuloop(self):
        running = True 
        background = Background(self.screen, "assets/background.png")
        back_move = Movement(background.x, background.y)
        clock = pygame.time.Clock()
        
        while running:
            background.drawBackground()
            background.x = back_move.backgroundMove()
            pygame.display.flip()
            clock.tick(30)
            self.screen.fill("black")



        
        
    def gameloop(self):
        pass
    
    def endloop(self):
        pass