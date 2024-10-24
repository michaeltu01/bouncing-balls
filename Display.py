"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

Display.py

Description: Handles the display of the bouncing balls.

"""

import random
import pymunk
import pygame

class PyGameDisplay:

    def __init__(self, win_width: int, win_height: int) -> None:
        self.win_width = win_width
        self.win_height = win_height
        self._screen = pygame.display.set_mode((win_width, win_height))

    def draw_balls(self, balls: list[pymunk.Circle, tuple], radius: int) -> None:
        """
        Draw the given balls with a given radius on the pygame screen.
        """
        for ball, color in balls:
            pos_x = int(ball.body.position.x)
            pos_y = int(ball.body.position.y)
            pygame.draw.circle(self._screen, color, (pos_x, pos_y), radius)

    def fill(self, color: tuple) -> None:
        """
        Fill the screen with the given color. Interface to the PyGame function of the same name.
        """
        self._screen.fill(color)



class PyMunkSpace:

    def __init__(self, win_width: int, win_height: int) -> None:
        self.win_width = win_width
        self.win_height = win_height
        self._space = self.setup_space(pymunk.Space(), win_width, win_height)

    def setup_space(self, space: pymunk.Space, width, height, e=0.9) -> pymunk.Space:
        """
        Create and return the pymunk space.
        """
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

        bottom_side = pymunk.Segment(space.static_body, (0, self.win_height), (width, height), SIDE_THICKNESS)
        bottom_side.elasticity = e
        bottom_side.friction = 0
        space.add(bottom_side)

        return space
    
    def create_ball(self, pos: tuple, v0: tuple, e=0.9) -> pymunk.Circle:
        """
        Arguments:
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
        self._space.add(body, shape)

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
    
    def step(self, dt: float) -> None:
        """
        Step the PyMunk space. Interface to the PyGame function of the same name.
        """
        self._space.step(dt)

    # def draw_button(pos: tuple, width: int, height: int, color: tuple, text: str) -> None:
    #     """
    #     Draw a button on the screen.
    #     """
    #     x, y = pos
    #     rect = pygame.Rect(x, y, width, height)
    #     pygame.draw.rect(screen, color, rect)
    #     screen.blit(pygame.font.SysFont("Arial", 20).render(text, True, (255, 255, 255)), (width/2, height/2))