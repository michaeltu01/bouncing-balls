"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

BallManager.py

Description: Manages the balls in the simulation.

"""

import queue
from ProcessMonitor import Message
from Ball import Ball
from util import total_runtime

class BallManager:
    def __init__(self, queue: queue.Queue[Message]) -> None:
        self._queue = queue
        self.balls = []
    
    def add_ball(self, ball: Ball) -> None:
        """
        Add ball to the existing set of balls.
        """
        self.balls.append(ball)
    
    def remove_ball(self, pid: int) -> None:
        """
        Remove ball by a given pid from the existing set of balls.
        """

    def update_ball(self, pid: int, ball: Ball) -> None:
        """
        Update ball in the existing set of balls.
        """
    
    def process_queue(self) -> list[Ball]:
        """
        Process the queue of balls.
        """
        for message in self._queue:
            mem_pct = message.data.memory_percent
            runtime = total_runtime(message.data.cpu_times)

            if message.action == "add":
                ball = Ball(message.pid, mem_pct, runtime)
                self.add_ball(ball)
            elif message.action == "remove":
                self.remove_ball(message.pid)
            elif message.action == "update":
                ball = Ball(message.pid, mem_pct, runtime)
                self.update_ball(message.pid, ball)
        
        return self.balls