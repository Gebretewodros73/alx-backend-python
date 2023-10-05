#!/usr/bin/env python3
"""
Module for element length calculation
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the
    original list `lst` and its length.

    Args:
        lst: An iterable of sequences

    Returns:
        A list of tuples where each tuple contains an element and its length
    """
    return [(i, len(i)) for i in lst]
