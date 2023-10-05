#!/usr/bin/env python3
"""
Module for safe first element retrieval
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input list or None if the list is empty.

    Args:
        lst: A sequence of elements.

    Returns:
        The first element of the list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
