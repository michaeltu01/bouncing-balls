import psutil
from collections import namedtuple

"""

UTILITY TYPES

"""

Position = namedtuple("Position", ["x", "y"])

"""

UTILITY FUNCTIONS

"""

def total_runtime(cpu_times) -> float:
    """
    Calculate the total runtime of the process in seconds.
    """
    # print(cpu_times)
    return cpu_times.user + cpu_times.system