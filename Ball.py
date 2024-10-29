"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

Ball.py

Description: Represents a ball in the simulation.

"""

import math
from util import Position
import pymunk

class Ball:
    def __init__(self, pid: int, memory_percent: float, runtime: float) -> None:
        self.pid = pid
        self.memory_percent = memory_percent
        self.runtime = runtime
        self.color = self.assign_color(pid)
        self.radius = self.size(memory_percent)
        self.velocity = self.init_vel(runtime)
        self.position: pymunk.Vec2d = None
        self.shape: pymunk.Circle = None

    def assign_color(self, pid: int) -> tuple[int, int, int]:
        """
        Assign a color to the ball based on its pid.
        """
        # colors = { # NO WHITE!! 
        #     "red": (255, 0, 0),
        #     "green": (0, 255, 0),
        #     "blue": (0, 0, 255),
        #     "yellow": (255, 255, 0),
        #     "purple": (255, 0, 255),
        #     "orange": (255, 165, 0),
        #     "cyan": (0, 255, 255),
        #     "magenta": (255, 0, 255),
        #     "black": (0, 0, 0),
        # }

        # color = random.choice(list(colors.values()))

        ratio = min(1, max(0, pid / 32768))  # 32768 = 2^15 (read from /proc/sys/kernel/pid_max)
        red = int(255 * (1 - ratio))
        green = 0
        blue = 0

        return (red, green, blue)
    
    def set_position(self, x: float, y: float) -> None:
        """
        Set the position of the ball.
        """
        # self.position = Position(x, y)
        self.position = pymunk.Vec2d(x, y)

    def assign_shape(self, shape: pymunk.Circle) -> None:
        """
        Assign the PyMunk shape to the ball.
        """
        self.shape = shape

    # FIXME: size() is currently mocked
    def size(self, memory_percent: float) -> int:
        """
        Assign a size to the ball based on its memory percentage.
        """
        return 40

    # FIXME: init_vel() is currently mocked
    def init_vel(self, runtime: float) -> tuple[float, float]:
        """
        Assign an initial velocity to the ball based on its runtime.
        """
        # return (400 * math.cos(45), 400 * math.sin(45))
        return (1, 0)

    def __str__(self) -> str:
        """
        To string method.
        """
        return f"Ball(pid={self.pid}, memory_percent={self.memory_percent}, runtime={self.runtime})"
    
