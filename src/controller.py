import pygame
from src.background import Background
from src.movement import Movement
from src.ground import Ground


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
        clock = pygame.time.Clock()
        
        
        background1 = Background(self.screen, "assets/background.png")
        back1_move = Movement(background1.x, background1.y, background1.image)
        background_width, background_height = background1.image.get_size()
        background2 = Background(self.screen, "assets/background.png", background_width)
        back2_move = Movement(background2.x, background2.y, background2.image)
        
        ground1 = Ground(self.screen, "assets/ground.png", 0, background_height)
        ground1_move = Movement(ground1.x, ground1.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()        
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.x, ground2.y, ground2.image)
        ground3 = Ground(self.screen, "assets/ground.png", (2 * ground_width), background_height)
        ground3_move = Movement(ground3.x, ground3.y, ground3.image)

        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        
        while running :
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.x = ground2_move.groundMove()
            ground3.drawGround()
            ground3.x = ground3_move.groundMove()

            
            
            pygame.display.flip()
            clock.tick(20)
            






        
        
    def gameloop(self):
        pass
    
    def endloop(self):
        pass