import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Snake speed
snake_speed = 15

# Snake coordinates
snake_coords = [[100, 50], [60, 50]]

# Food coordinates
food_x = random.randint(0, screen_width - 10)
food_y = random.randint(0, screen_height - 10)

# Game Loop
while True:
    # Draw screen
    screen.fill(BLACK)

    # Draw snake
    for coord in snake_coords:
        pygame.draw.rect(screen, GREEN, [coord[0], coord[1], 10, 10])

    # Draw food
    pygame.draw.rect(screen, RED, [food_x, food_y, 10, 10])

    # Update screen
    pygame.display.update()
