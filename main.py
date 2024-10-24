"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.


main.py

Description: The main game loop for the bouncing balls simulation.

Sources:
- Myself
- https://nbviewer.org/github/alessandro-giusti/bouncing-ball-patterns/blob/main/bouncing.ipynb
- https://www.youtube.com/watch?v=YrNpkuVIFdg

"""


import pygame
import sys
import math
from Display import PyGameDisplay, PyMunkSpace
from ProcessMonitor import ProcessMonitor
import queue

"""

Main functionality

"""

# General setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
WIN_HEIGHT = 800
WIN_WIDTH = 800
screen = PyGameDisplay(WIN_WIDTH, WIN_HEIGHT)

# Create the physics space
space = PyMunkSpace(WIN_WIDTH, WIN_HEIGHT)

# Create the balls
RADIUS = 40
balls = []

# Initialize the ProcessMonitor
message_queue = queue.Queue()
monitor = ProcessMonitor(message_queue)
monitor.populate_queue()

# Main game loop
while True:
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Add a new ball on click
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(space.create_ball(event.pos, (400 * math.cos(45), 400 * math.sin(45))))
            # if 50 <= event.pos[0] <= 300 and 50 <= event.pos[1] <= 150:
            #     balls.append(create_ball(space, event.pos, (400 * math.cos(45), 400 * math.sin(45))))

    # Update the screen
    screen.fill((255, 255, 255)) # background color
    # draw_button((50, 50), 250, 100, (0, 0, 255), "Add ball")
    screen.draw_balls(balls, RADIUS)    
    space.step(1/60) # 60 FPS
    clock.tick(60) # 60 FPS
    pygame.display.update()