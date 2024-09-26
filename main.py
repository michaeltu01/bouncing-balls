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
def create_ball(space: pymunk.Space):
    """
    Create a ball in the given space.
    """
    body = pymunk.Body(_, _, body_type=pymunk.Body.DYNAMIC)
    pass

def draw_balls(balls: list[pymunk.Circle], radius: int) -> None:
    """
    Draw the given balls with a given radius on the pygame screen.
    """
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), radius)


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
space.gravity = (150, 150) # (gravity_X, gravity_Y)

# Create the balls
RADIUS = 40

balls = []
balls.append(create_ball(space))
draw_balls(balls, RADIUS)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255)) # background color
    space.step(1/60)
    pygame.display.update()
    clock.tick(60) # 60 FPS
