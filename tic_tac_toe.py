import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up font
font = pygame.font.SysFont(None, 100)

# Render font
start_text = font.render("Start Game", True, BLACK)


running = True
start_screen_run = True


# Start screen
while start_screen_run:
    # Create a rectangle with (top-leftx, top-lefty, width, height)
    start_rect = pygame.Rect(200, 300, 400, 100)

    # Goes over the events
    for event in pygame.event.get():
        # Press the quit button at the top
        if event.type == pygame.QUIT:
            start_screen_run = False
            running = False
        
        # Check if the mouse is clicking the start_rect rectangle
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                start_screen_run = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, start_rect)
    
    # Write the text
    screen.blit(start_text, (200, 300))
    
    # Update the display
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Drawing lines
    for i in range(4):
        pygame.draw.line(screen, BLACK, (150, 50+150*i), (600, 50+150*i), 10)
        pygame.draw.line(screen, BLACK, (150+150*i, 50), (150+150*i, 500), 10)

    pygame.display.flip()
pygame.quit()

