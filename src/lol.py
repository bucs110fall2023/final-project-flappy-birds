import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectangle Border")

# Define rectangle parameters (position, size, color, etc.)
rect_x = 100
rect_y = 100
rect_width = 200
rect_height = 150
border_width = 4  # Adjust the border width as needed
rect_color = (255, 0, 0)  # Red color, format: (R, G, B)
border_color = (0, 0, 255)  # Blue color for the border

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the inner rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Draw the outer border
    pygame.draw.rect(screen, border_color, (rect_x - border_width, rect_y - border_width,
                                            rect_width + 2 * border_width, rect_height + 2 * border_width), border_width)

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
