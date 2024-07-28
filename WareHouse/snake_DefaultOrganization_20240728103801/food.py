'''
This file contains the Food class.
'''
import pygame
class Food:
    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
    def draw(self, game_window):  # Add game_window parameter
        pygame.draw.rect(game_window, white, [self.x, self.y, self.block_size, self.block_size])