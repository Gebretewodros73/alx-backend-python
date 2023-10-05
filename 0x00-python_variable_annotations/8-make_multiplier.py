#!/usr/bin/env python3
"""
Module for creating a multiplier function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by `multiplier`

    Args:
        multiplier: A float value

    Returns:
        A function that takes a float and returns the product
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
