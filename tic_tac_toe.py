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
    start_rect = pygame.Rect(200, 300, 400, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen_run = False
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                start_screen_run = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, start_rect)
    screen.blit(start_text, (200, 300))
    
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.display.flip()
pygame.quit()

