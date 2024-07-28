'''
This file contains the Snake class.
'''
import pygame
class Snake:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.block_size = block_size
    def move_left(self):
        self.x_change = -self.block_size
        self.y_change = 0
    def move_right(self):
        self.x_change = self.block_size
        self.y_change = 0
    def move_up(self):
        self.y_change = -self.block_size
        self.x_change = 0
    def move_down(self):
        self.y_change = self.block_size
        self.x_change = 0
    def update_position(self):
        self.x += self.x_change
        self.y += self.y_change
    def draw(self, game_window):  # Add game_window parameter
        pygame.draw.rect(game_window, green, [self.x, self.y, self.block_size, self.block_size])