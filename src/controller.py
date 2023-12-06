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
        ground1_move = Movement(ground1.rect.x, ground1.rect.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()        
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.rect.x, ground2.rect.y, ground2.image)
        
        
        play_buttonimg = pygame.image.load("assets/button.png")
        scaled_button = pygame.transform.scale(play_buttonimg, (background_width/6, ground_height))

        font_size = int(background_width/6)
        custom_font = pygame.font.Font('assets/FlappyBirdy.ttf', font_size)
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
            ground1.rect.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.rect.x = ground2_move.groundMove()
        
            if play_button_draw == True:
                
                text_rendered = custom_font.render(text, True, "black")  
                self.screen.blit(text_rendered, (background_width/4, background_height/3))
                play_button = pygame.draw.rect(self.screen, (223, 218, 151), ((background_width/3) - 10 , (background_height + ground_height)/2, background_width/6, ground_height))
                border_play_button = pygame.draw.rect(self.screen, "black", (((background_width/3) - 10) - border_width , ((background_height + ground_height)/2)- border_width , (background_width/6) + (2* border_width), (ground_height) + (2* border_width)), border_width)
                self.screen.blit(scaled_button, ((background_width/3) - 10 , (background_height + ground_height)/2))
                
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
        ground1_move = Movement(ground1.rect.x, ground1.rect.y, ground1.image)
        ground_width, ground_height = ground1.image.get_size()        
        ground2 = Ground(self.screen, "assets/ground.png", ground_width, background_height)
        ground2_move = Movement(ground2.rect.x, ground2.rect.y, ground2.image)
        
        bottompipe = Pipe(self.screen, "assets/bottompipe.png", background_width, 400)
        self.bottompipes.add(bottompipe)
        bottompipe2 = Pipe(self.screen, "assets/bottompipe.png", (background_width + (background_width)/2)-2 , 400)
        self.bottompipes.add(bottompipe2)
        
        toppipe = Pipe(self.screen, "assets/toppipe.png", background_width, -400)
        self.bottompipes.add(toppipe)
        toppipe2 = Pipe(self.screen, "assets/toppipe.png", (background_width + (background_width)/2)-2, -400)
        self.bottompipes.add(toppipe2)
        
        game_bird = Bird(self.screen, "assets/blueflappybird.png",(background_width/3) , background_height/2 )
        bird_move = Movement(game_bird.rect.x, game_bird.rect.y)
        bird_move.t = 0
        
        font_size = int(background_width/8)
        custom_font = pygame.font.Font('assets/flappybirdnums.ttf', font_size)
        self.score_count = 0
        score = str(self.score_count)        

        self.screen = pygame.display.set_mode((background_width, background_height + ground_height ))
        print(background_width)
        
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
            ground1.rect.x = ground1_move.groundMove()
            ground2.drawGround()
            ground2.rect.x = ground2_move.groundMove()
            
            y = random.randint(int(((1/3)*(background_height))+35),int(background_height-35))
            for b in self.bottompipes:
                
                pipe_move = Movement(b.rect.x, b.rect.y)
                b.drawPipe()
                b.rect.x = pipe_move.pipeMove()   

                if b.rect.x < -100:

                    b.kill()
                    self.bottompipes.remove(b)
                    
                    space_in_between = 200
                    
                    if b.imgpath == "assets/bottompipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/bottompipe.png", background_width, y))
                    if b.imgpath == "assets/toppipe.png":
                        self.bottompipes.add(Pipe(self.screen, "assets/toppipe.png", background_width, y - space_in_between - b.image.get_size()[1]))

                if pygame.sprite.collide_rect(game_bird, b):
                    self.state = "END"
                    
                if int(b.rect.x) == int(game_bird.rect.x):
                    self.score_count += 0.5
                    score = str(int(self.score_count))                  
                    
            if pygame.sprite.collide_rect(game_bird, ground1):
                self.state = "END"
            elif pygame.sprite.collide_rect(game_bird, ground2):
                self.state  = "END"
            
            
            bird_move.t += 1/40
            
            game_birdspeed = bird_move.birdSpeed()

            
            if int(game_birdspeed) > 0:
                game_bird.rect.y = bird_move.birdFall()
                game_bird.rotation_angle -= 5
                if game_bird.rotation_angle < -90:
                    game_bird.rotation_angle = -90
                    
            elif int(game_birdspeed) < 0:
                game_bird.rect.y = bird_move.birdJump()
                game_bird.rotation_angle += 20
                if game_bird.rotation_angle > 45:
                    game_bird.rotation_angle = 45

                
            game_bird.drawJumpBird()
    
            text_rendered = custom_font.render(score, True, "black")  
            self.screen.blit(text_rendered, ((4*background_width)/9, background_height/12))
                  
            pygame.display.flip()
            clock.tick(60)
          
    def endloop(self):
        while self.state == "END":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()