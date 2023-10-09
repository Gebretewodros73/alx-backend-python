#!/usr/bin/env python3
"""
Module for Task 1
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays (float values) in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
