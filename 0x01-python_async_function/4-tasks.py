#!/usr/bin/env python3
"""module for multiple concurrent coroutines"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments (in this order):
        n and max_delay, and spawns wait_random n times
        with the specified max_delay
    """
    routines = []
    for i in range(n):
        routines.append(task_wait_random(max_delay))
    delays = sorted(await asyncio.gather(*routines))
    return delays
