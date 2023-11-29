import pygame
from src.background import Background
from src.movement import Movement




class Controller:


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        
    
    def mainloop(self):
        running = True
        while running:
            
            for event in pygame.event.get():
                pass


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
        background1 = Background(self.screen, "assets/background.png")
        back1_move = Movement(background1.x, background1.y)
        
        screen_width, screen_height = background1.image.get_size()
        
        background2 = Background(self.screen, "assets/background.png")
        back2_move = Movement(background2.x + screen_width, background2.y)
        
        
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        
        while running :
            
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()

            
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
          
            
            if abs(background1.x) > screen_width:
                background1.x = screen_width
            elif abs(background2.x) > screen_width:
                background2.x = screen_width
            
            pygame.display.flip()
            clock.tick(30)
            self.screen.fill("black")




        
        
    def gameloop(self):
        pass
    
    def endloop(self):
        pass