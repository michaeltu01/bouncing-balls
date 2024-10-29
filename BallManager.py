"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

BallManager.py

Description: Manages the balls in the simulation.

"""

import queue
from ProcessMonitor import Message
import time
from Ball import Ball
from util import total_runtime

class BallManager:
    def __init__(self, queue: queue.Queue[Message]) -> None:
        self._queue = queue
        self.balls = {}  # {pid: ball}
        self.last_update_time = time.time()

        # FIXME: Move this variable to the correct location
        self.update_interval = 1
    
    def add_ball(self, pid: int, ball: Ball) -> None:
        """
        Add ball to the existing set of balls.
        """
        self.balls[pid] = ball
    
    def remove_ball(self, pid: int) -> None:
        """
        Remove ball by a given pid from the existing set of balls.
        """
        self.balls.pop(pid)

    def update_ball(self, pid: int, ball: Ball) -> None:
        """
        Update ball in the existing set of balls.
        """
        self.balls[pid] = ball
    
    def process_queue(self) -> list[Ball]:
        """
        Process the queue of balls.
        """

        # FIXME: Process the queue for UPDATE_TIME amount of time
        cur_time = time.time()
        while cur_time - self.last_update_time < self.update_interval:
            try:
                message = self._queue.get_nowait()
            except queue.Empty:  # if the queue is empty, then just return
                break

            mem_pct = message.data.memory_percent
            runtime = total_runtime(message.data.cpu_times)

            if message.action == "add":
                ball = Ball(message.pid, mem_pct, runtime)
                self.add_ball(message.pid, ball)
            elif message.action == "remove":
                self.remove_ball(message.pid)
            elif message.action == "update":
                ball = Ball(message.pid, mem_pct, runtime)
                self.update_ball(message.pid, ball)
            
            cur_time = time.time()
        
        self.last_update_time = cur_time
        return list(self.balls.values())  # return a list of balls from self.balls