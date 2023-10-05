#!/usr/bin/env python3
"""
Module for converting a string and a number to a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number to a tuple

    Args:
        k: A string
        v: An int or float

    Returns:
        A tuple containing the string `k` and the square of `v`
    """
    return (k, v ** 2)
