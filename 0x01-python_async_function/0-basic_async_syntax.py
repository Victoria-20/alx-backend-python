#!/usr/bin/env python3
""" module for an asynchronous coroutine"""
import syncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ takes in an integer argument (max_delay, 
        with a default value of 10) named wait_random that 
        waits for a random delay between 0 and max_delay
    """
    value = random.uniform(0, max_delay + 1)
    await asyncio.sleep(value)
    return value
