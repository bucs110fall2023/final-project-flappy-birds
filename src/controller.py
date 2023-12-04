import pygame
import random
from src.background import Background
from src.movement import Movement
from src.ground import Ground
from src.pipe import Pipe
from src.bird import Bird


class Controller:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        
        self.bottompipes = pygame.sprite.Group()
    
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
        
        font_path = 'assets/FlappyBirdy.ttf'
        font_size = int(background_width/6)
        custom_font = pygame.font.Font(font_path, font_size)
        text = "Jumpy Birdy"
        
        border_width = 5

        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        
        bird = None
        bird_drawn = False
        play_button_draw = True
        exit_button_draw = True
        
        
        while self.state == "MENU" :
            
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.x = ground2_move.groundMove()
            


            
          
            if play_button_draw == True:
                
                text_rendered = custom_font.render(text, True, "black")  
                self.screen.blit(text_rendered, (background_width/4, background_height/3))
                play_button = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/3) - 10 , (background_height + ground_height)/2, background_width/6, ground_height))
                border_play_button = pygame.draw.rect(self.screen, "black", (((background_width/3) - 10) - border_width , ((background_height + ground_height)/2)- border_width , (background_width/6) + (2* border_width), (ground_height) + (2* border_width)), border_width)
                
            if exit_button_draw == True:
                exit_button = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/2) + 10, (background_height + ground_height)/2, background_width/6, ground_height))
                exit_button_border = pygame.draw.rect(self.screen, "black", (((background_width/2) + 10) - border_width , ((background_height + ground_height)/2) - border_width, (background_width/6) + (2* border_width), (ground_height)+ (2* border_width)), border_width)
                
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        play_button_draw = False
                        exit_button_draw = False
                        bird = Bird(self.screen, "assets/blueflappybird.png",background_width/3, background_height/2 )
                        bird_drawn = True
                    elif exit_button.collidepoint(event.pos):
                        pygame.quit()
                if event.type == pygame.QUIT:
                        pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if bird:
                        print("hi")
                        bird.kill()
                        self.state = "GAME"
                        
            if bird_drawn == True:
                bird.drawBird()
                
            pygame.display.flip()
            clock.tick(60)
        
        
    def gameloop(self):
        
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
        
        bottompipe = Pipe(self.screen, "assets/bottompipe.png", background_width, 400)
        self.bottompipes.add(bottompipe)
        bottompipe2 = Pipe(self.screen, "assets/bottompipe.png", background_width + (background_width)/2 , 400)
        self.bottompipes.add(bottompipe2)
        
        toppipe = Pipe(self.screen, "assets/toppipe.png", background_width, -400)
        self.bottompipes.add(toppipe)
        toppipe2 = Pipe(self.screen, "assets/toppipe.png", background_width + (background_width)/2, -400)
        self.bottompipes.add(toppipe2)
        
        game_bird = Bird(self.screen, "assets/blueflappybird.png",background_width/3, background_height/2 )
        bird_move = Movement(game_bird.x, game_bird.y)
        bird_move.t = 0
        
        
        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        fall = True
        
        while self.state == "GAME" :
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird_move.t = 0
                elif event.type == pygame.QUIT:
                    pygame.quit()

            
            self.screen.fill("black")
            background1.drawBackground()
            background1.x = back1_move.backgroundMove()
            background2.drawBackground()
            background2.x = back2_move.backgroundMove()
            
            ground1.drawGround()
            ground1.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.x = ground2_move.groundMove()
            
            y = random.randint(int(((1/3)*(background_height))+35),int(background_height-35))
            for b in self.bottompipes:
                
                pipe_move = Movement(b.x, b.y)
                b.drawPipe()
                b.x = pipe_move.pipeMove()    

                if b.x < -200:
                    b.kill()
                    self.bottompipes.remove(b)
                    
                    space_in_between = 200
                    
                    if b.imgpath == "assets/bottompipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/bottompipe.png", background_width, y))
                    if b.imgpath == "assets/toppipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/toppipe.png", background_width, y - space_in_between - b.image.get_size()[1]))
            
            collisions = pygame.sprite.spritecollide(game_bird, self.bottompipes, False)

            if not collisions:
                print("BYEEEE")
            if game_bird.y > background_height:
                self.state = "END"
            
            game_bird.drawBird()
            bird_move.t += 1/40
            game_bird.y = bird_move.birdJump()
            

            


                    
            pygame.display.flip()
            clock.tick(60)
            
            
        
    
    def endloop(self):
        pygame.quit()