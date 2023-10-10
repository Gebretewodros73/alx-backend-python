#!/usr/bin/env python3
"""
Task 0's module.
"""


import asyncio
import random


async def async_generator() -> float:
    """Yields 10 random numbers between 0 and 10,
    with a 1 second delay each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# For testing
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
