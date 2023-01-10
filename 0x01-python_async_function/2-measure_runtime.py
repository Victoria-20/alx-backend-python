#!/usr/bin/env python3
"""Module to measure the run time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    initial_t = time.time()
    asyncio.run(wait_n(n, max_delay))

    end_t = time.time()
    return ((end_t - initial_t) / n)
