"""
This is the main file of the Snake Game.
"""

import pygame
import sys
import time
import random

# Initialize pygame
pygame.init()
# Set the width and height of the game window
window_width = 800
window_height = 600
# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
# Set the size of each grid block
block_size = 20
# Set the speed of the snake
snake_speed = 10
# Set the font style and size
font_style = pygame.font.SysFont(None, 50)
# Set the score font style and size
score_font = pygame.font.SysFont(None, 35)
# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")


# Define the snake function
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])


# Define the game loop function
def game_loop():
    game_over = False
    game_close = False
    # Set the initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    # Set the initial change in position of the snake
    x1_change = 0
    y1_change = 0
    # Create the snake list and set the initial length of the snake
    snake_List = []
    Length_of_snake = 1
    # Set the initial position of the food
    foodx = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
    # Game loop
    while not game_over:
        while game_close == True:
            game_window.fill(black)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            # Check for user input after losing the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        # Check for user input during the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
        # Check if the snake hits the boundaries of the game window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        game_window.fill(black)
        pygame.draw.rect(game_window, white, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # Check if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        # Draw the snake
        snake(block_size, snake_List)
        # Update the score
        score(Length_of_snake - 1)
        # Update the game window
        pygame.display.update()
        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1
        # Set the speed of the game
        clock = pygame.time.Clock()
        clock.tick(snake_speed)
    # Quit pygame and exit the program
    pygame.quit()
    sys.exit()


# Define the function to display messages on the game window
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])


# Define the function to display the score on the game window
def score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    game_window.blit(value, [0, 0])


# Run the game loop
game_loop()
