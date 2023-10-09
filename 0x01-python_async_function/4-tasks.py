#!/usr/bin/env python3
"""
Module for Task 4
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """
    Returns a list of asyncio.Tasks.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[asyncio.Task]: List of tasks that wait for a random delay.
    """
    return [task_wait_random(max_delay) for _ in range(n)]
