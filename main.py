"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

Description: A bouncing balls game to pass the time.

Sources:
- Myself
- https://nbviewer.org/github/alessandro-giusti/bouncing-ball-patterns/blob/main/bouncing.ipynb
- https://www.youtube.com/watch?v=YrNpkuVIFdg

"""


import random
import pygame
import sys
import pymunk
import math

"""

HELPER FUNCTIONS

"""
def create_ball(space: pymunk.Space, pos: tuple, v0: tuple, e=0.9) -> pymunk.Circle:
    """
    Arguments:
    - space (pymunk.Space): the physics space
    - pos (tuple): the position of the ball
    - v0 (tuple): the initial velocity of the ball
    - e (float): the elasticity of the ball

    Create a ball in the given space.
    """
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    body.velocity = v0

    shape = pymunk.Circle(body, 40)
    shape.elasticity = e
    space.add(body, shape)

    colors = { # NO WHITE!! 
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (255, 0, 255),
        "orange": (255, 165, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "black": (0, 0, 0),
    }

    color = random.choice(list(colors.values()))
    return shape, color

def draw_balls(balls: list[pymunk.Circle, tuple], radius: int) -> None:
    """
    Draw the given balls with a given radius on the pygame screen.
    """
    for ball, color in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, color, (pos_x, pos_y), radius)

def setup_space(width, height, e=0.9) -> pymunk.Space:
    """
    Create and return the pymunk space.
    """
    space = pymunk.Space()
    space.gravity = (0, 982) # (gravity_X, gravity_Y)

    # Create the sides of the window
    SIDE_THICKNESS = 5

    right_side = pymunk.Segment(space.static_body, (width, 0), (width, height), SIDE_THICKNESS)
    right_side.elasticity = e
    right_side.friction = 0
    space.add(right_side)

    left_side = pymunk.Segment(space.static_body, (0, 0), (0, height), SIDE_THICKNESS)
    left_side.elasticity = e
    left_side.friction = 0
    space.add(left_side)

    top_side = pymunk.Segment(space.static_body, (0, 0), (width, 0), SIDE_THICKNESS)
    top_side.elasticity = e
    top_side.friction = 0
    space.add(top_side)

    bottom_side = pymunk.Segment(space.static_body, (0, WIN_HEIGHT), (width, height), SIDE_THICKNESS)
    bottom_side.elasticity = e
    bottom_side.friction = 0
    space.add(bottom_side)

    return space

def draw_button(pos: tuple, width: int, height: int, color: tuple, text: str) -> None:
    """
    Draw a button on the screen.
    """
    x, y = pos
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    screen.blit(pygame.font.SysFont("Arial", 20).render(text, True, (255, 255, 255)), (width/2, height/2))

"""

Main functionality

"""

# General setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
WIN_HEIGHT = 800
WIN_WIDTH = 800
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# Create the physics space
space = setup_space(WIN_WIDTH, WIN_HEIGHT)

# Create the balls
RADIUS = 40
balls = []

# Main game loop
while True:
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Add a new ball on click
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(create_ball(space, event.pos, (400 * math.cos(45), 400 * math.sin(45))))
            # if 50 <= event.pos[0] <= 300 and 50 <= event.pos[1] <= 150:
            #     balls.append(create_ball(space, event.pos, (400 * math.cos(45), 400 * math.sin(45))))

    # Update the screen
    screen.fill((255, 255, 255)) # background color
    # draw_button((50, 50), 250, 100, (0, 0, 255), "Add ball")
    draw_balls(balls, RADIUS)    
    space.step(1/60) # 120 FPS
    clock.tick(60) # 120 FPS
    pygame.display.update()