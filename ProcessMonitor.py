"""

Bouncing Balls Assignment, CSCI 2340, Fall 2024
Author: Michael Tu (mstu)

Copyright (c) 2024, Michael Tu, All Rights Reserved. CSCI 2340, Fall 2024, All Rights Reserved.

ProcessMonitor.py

Description: Monitors the running processes.

"""

from dataclasses import dataclass
import psutil
import queue

@dataclass
class MessageData:
    username: str
    cpu_percent: float
    memory_percent: float
    cpu_times: float

@dataclass
class Message:
    action: str
    pid: int
    data: MessageData

class ProcessMonitor:

    def __init__(self, queue: queue.Queue) -> None:
        self._queue = queue  # Collection of processes
    
    def populate_queue(self) -> None:
        """
        Populate the queue with processes at the start of the simulation.
        """
        attrs = ['username', 'pid', 'cpu_percent', 'memory_percent', 'memory_info', 'cpu_times']
        procs = {p.pid: p.info for p in psutil.process_iter(attrs)}

        for pid, proc in procs.items():
            proc_data = MessageData(username=proc['username'], cpu_percent=proc['cpu_percent'], memory_percent=proc['memory_percent'], cpu_times=proc['cpu_times'])
            self._queue.put(Message(action="add", pid=pid, data=proc_data))
        
        print(self._queue)