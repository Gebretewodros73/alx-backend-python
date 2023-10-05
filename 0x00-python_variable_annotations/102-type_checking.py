#!/usr/bin/env python3
"""
Module for zooming in an array.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on the elements of the input list.

    Args:
        lst (Tuple): The input list.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
