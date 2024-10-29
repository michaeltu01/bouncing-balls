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
from Ball import Ball


"""

CONSTANTS

"""
RADIUS_SCALE_DOWN_FACTOR = 0.05
ELASTICITY = 0.9


"""

CLASSES

"""

class PyGameDisplay:

    def __init__(self, win_width: int, win_height: int) -> None:
        self.win_width = win_width
        self.win_height = win_height

        # Initialize pygame
        pygame.init()
        self._screen = pygame.display.set_mode((win_width, win_height))
        self.clock = pygame.time.Clock()

    # def draw_balls(self, balls: list[pymunk.Circle, tuple], radius: int) -> None:
    #     """
    #     Draw the given balls with a given radius on the pygame screen.
    #     """
    #     for ball, color in balls:
    #         pos_x = int(ball.body.position.x)
    #         pos_y = int(ball.body.position.y)
    #         pygame.draw.circle(self._screen, color, (pos_x, pos_y), radius)

    def _draw_ball(self, ball: Ball) -> None:
        """
        Private function for drawing a single ball on the pygame screen.

        Throws an Exception if ball's position is None.
        """
        if ball.position is None:
            raise Exception(f"Ball PID {ball.pid} position is None")
        pos_x = int(ball.shape.body.position.x)
        pos_y = int(ball.shape.body.position.y)
        # print(pos_x, pos_y)
        pygame.draw.circle(self._screen, ball.color, (pos_x, pos_y), ball.radius)

    def draw_balls(self, balls: list[Ball]) -> None:
        """
        Draw the given balls with a given radius on the pygame screen.
        """
        for ball in balls:
            self._draw_ball(ball)

    def fill(self, color: tuple) -> None:
        """
        Fill the screen with the given color. Interface to the PyGame function of the same name.
        """
        self._screen.fill(color)

    def update(self) -> None:
        """
        Update the pygame screen. Interface to the PyGame function of the same name.
        """
        pygame.display.update()



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
        # space.damping = 0.9999
        static_body = space.static_body

        # Create the sides of the window
        SIDE_THICKNESS = 5

        right_side = pymunk.Segment(static_body, (width, 0), (width, height), SIDE_THICKNESS)
        right_side.elasticity = e
        right_side.friction = 0
        space.add(right_side)

        left_side = pymunk.Segment(static_body, (0, 0), (0, height), SIDE_THICKNESS)
        left_side.elasticity = e
        left_side.friction = 0
        space.add(left_side)

        top_side = pymunk.Segment(static_body, (0, 0), (width, 0), SIDE_THICKNESS)
        top_side.elasticity = e
        top_side.friction = 0
        space.add(top_side)

        bottom_side = pymunk.Segment(static_body, (0, self.win_height), (width, height), SIDE_THICKNESS)
        bottom_side.elasticity = e
        bottom_side.friction = 0
        space.add(bottom_side)

        return space
    
    # def create_ball(self, pos: tuple, v0: tuple, e=0.9) -> pymunk.Circle:
    #     """
    #     Arguments:
    #     - pos (tuple): the position of the ball
    #     - v0 (tuple): the initial velocity of the ball
    #     - e (float): the elasticity of the ball

    #     Create a ball in the given space.
    #     """
    #     body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    #     body.position = pos
    #     body.velocity = v0

    #     shape = pymunk.Circle(body, 40)
    #     shape.elasticity = e
    #     self._space.add(body, shape)

    #     return shape

    def _create_ball(self, ball: Ball) -> None:
        """
        Private function to create a ball in the PyMunk space.
        """
        body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
        if ball.position is None:
            rand_x, rand_y = random.randint(0, self.win_width), random.randint(0, self.win_height)
            print(f"Setting initial ball position: {rand_x}, {rand_y}")
            ball.set_position(rand_x, rand_y)
            body.position = pymunk.Vec2d(rand_x, rand_y)
        else:
            raise Exception("Ball position must be None to create a new ball")
            # ball.set_position(rand_x, rand_y)
        # body.position = pymunk.Vec2d(ball.position.x, ball.position.y)
        # body.position = ball.position
        body.velocity = ball.velocity

        shape = pymunk.Circle(body, ball.radius)
        shape.elasticity = ELASTICITY
        ball.assign_shape(shape)  # This is how PyMunk will update the ball
        self._space.add(body, shape)

    def create_balls(self, balls: list[Ball]) -> None:
        """
        Create a collection of balls in the PyMunk space.
        """
        for ball in balls:
            self._create_ball(ball)
    
    def step(self, dt: float) -> None:
        """
        Step the PyMunk space. Interface to the PyGame function of the same name.
        """
        self._space.step(dt)

    def debug_draw(self, options: pymunk.SpaceDebugDrawOptions) -> None:
        """
        Draw the PyMunk space. Interface to the PyGame function of the same name.
        """
        self._space.debug_draw(options)