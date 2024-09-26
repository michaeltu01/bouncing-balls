"""

[INSERT CLASS DOCSTRING]

"""

"""

[COPYRIGHT STATEMENT]

"""


import pygame
import sys
import pymunk


"""

HELPER FUNCTIONS

"""
def create_ball(space: pymunk.Space) -> pymunk.Circle:
    """
    Create a ball in the given space.
    """
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (400, 400)
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape

def draw_balls(balls: list[pymunk.Circle], radius: int) -> None:
    """
    Draw the given balls with a given radius on the pygame screen.
    """
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0, 0, 255), (pos_x, pos_y), radius)


"""

Initialize Pygame and Pymunk

"""

# General setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
screen = pygame.display.set_mode((800,800))

# Create the physics space
space = pymunk.Space()
space.gravity = (0, 500) # (gravity_X, gravity_Y)

# Create the balls
RADIUS = 40
balls = []
balls.append(create_ball(space))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255)) # background color
    draw_balls(balls, RADIUS)
    space.step(1/60)
    pygame.display.update()
    clock.tick(120) # 60 FPS
