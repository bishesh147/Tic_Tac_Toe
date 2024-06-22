import pygame
import game_logic

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

font = pygame.font.SysFont(None, 230)
x_text = font.render("X", True, BLUE)
o_text = font.render("O", True, GREEN)

win_font = pygame.font.SysFont(None, 400)
x_win_text = win_font.render("X Wins", True, BLACK)
o_win_text = win_font.render("O Wins", True, BLACK)
draw_text = win_font.render("Draw", True, BLACK)


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


turn = True #True is for X move, False is for O move
game_status = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #Check for mouse button press
            mouse_pos = event.pos   # Get the position of the mouse click, gives a tuple
            mouse_pos = list(mouse_pos)
            if mouse_pos[0] >= 150 and mouse_pos[0] <= 600 and mouse_pos[1] >= 50 and mouse_pos[1] <= 500:
                y = (mouse_pos[0]-150)//150
                x = (mouse_pos[1]-50)//150
                if game_status[x][y] == ".":
                    if (turn):
                        game_status[x][y] = "X"
                        turn = False
                    else:
                        game_status[x][y] = "O"
                        turn = True

    screen.fill(WHITE)

    # Drawing lines
    for i in range(4):
        pygame.draw.line(screen, BLACK, (150, 50+150*i), (600, 50+150*i), 10)
        pygame.draw.line(screen, BLACK, (150+150*i, 50), (150+150*i, 500), 10)

    for i in range(3):
        for j in range(3):
            if game_status[i][j] == "X":
                screen.blit(x_text, (160+150*j, 60+150*i))
            if game_status[i][j] == "O":
                screen.blit(o_text, (160+150*j, 60+150*i))
    

    result = game_logic.determine_winner(game_status)
    if result[1] == 1:
        pygame.draw.line(screen, RED, (150, 50+75), (600, 50+75), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 2:
        pygame.draw.line(screen, RED, (150+75, 50), (150+75, 500), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 3:
        pygame.draw.line(screen, RED, (150, 50), (600, 500), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 4:
        pygame.draw.line(screen, RED, (150+75+150, 50), (150+75+150, 500), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 5:
        pygame.draw.line(screen, RED, (150+75+300, 50), (150+75+300, 500), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 6:
        pygame.draw.line(screen, RED, (150, 50+75+150), (600, 50+75+150), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
    elif result[1] == 7:
        pygame.draw.line(screen, RED, (150, 50+75+300), (600, 50+75+300), 10)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_status = [[".",".","."], [".",".","."], [".",".","."]]
        turn = True
     
    pygame.display.flip()
pygame.quit()

