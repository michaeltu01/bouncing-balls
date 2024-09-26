"""

[INSERT CLASS DOCSTRING]

"""

"""

[COPYRIGHT STATEMENT]

Sources:
- Myself
- https://nbviewer.org/github/alessandro-giusti/bouncing-ball-patterns/blob/main/bouncing.ipynb
- https://www.youtube.com/watch?v=YrNpkuVIFdg

"""


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
    return shape

def draw_balls(balls: list[pymunk.Circle], radius: int) -> None:
    """
    Draw the given balls with a given radius on the pygame screen.
    """
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), radius) # TODO: make color random

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


"""

Initialize Pygame and Pymunk

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

    screen.fill((255, 255, 255)) # background color
    draw_balls(balls, RADIUS)
    space.step(1/60)
    pygame.display.update()
    clock.tick(120) # 60 FPS
