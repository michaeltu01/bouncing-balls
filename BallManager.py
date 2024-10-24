"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

BallManager.py

Description: Manages the balls in the simulation.

"""

import queue

class BallManager:
    def __init__(self, queue: queue.Queue) -> None:
        self._queue = queue