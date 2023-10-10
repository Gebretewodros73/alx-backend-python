#!/usr/bin/env python3
'''
Measure Runtime Task
'''
from time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    '''
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()

    return end_time - start_time
