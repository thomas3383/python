import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
display_width = 600
display_height = 600

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Font and font size
font_style = pygame.font.SysFont(None, 30)

# Create a display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control game speed
clock = pygame.time.Clock()

# Function to display text on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, green)
    game_display.blit(value, [0, 0])

# Function to run the game
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial change in position
    x1_change = 0
    y1_change = 0

    # Snake's body (initially only the head)
    snake_list = []
    snake_length = 1

    # Initial position of food
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # Initial score
    score = 0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", green)
            Your_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake hits the boundary
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update snake's position
        x1 += x1_change
        y1 += y1_change
        game_display.fill(white)

        # Draw food
        pygame.draw.rect(game_display, green, [food_x, food_y, snake_block, snake_block])

        # Snake body mechanism
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        our_snake(snake_block, snake_list)
        
        # Display score
        Your_score(score)

        pygame.display.update()

        # If snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 1

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
