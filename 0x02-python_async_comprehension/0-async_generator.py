#!/usr/bin/env python3
'''
Async Generator Task
'''


import asyncio
import random


async def async_generator() -> float:
    '''
    Coroutine that yields 10 random
    numbers between 0 and 10 with 1 second delay.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
