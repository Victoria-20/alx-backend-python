#!/usr/bin/env python3
"""module for parallel comprehensions"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure total run time of four parallel comprehesions"""
    start = time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return (time() - start)
