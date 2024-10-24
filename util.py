import psutil

def total_runtime(cpu_times) -> float:
    """
    Calculate the total runtime of the process in seconds.
    """
    return cpu_times.user + cpu_times.system + cpu_times.idle