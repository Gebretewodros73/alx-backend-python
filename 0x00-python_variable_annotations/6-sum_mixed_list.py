#!/usr/bin/env python3
"""
Module for summing a list of mixed integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of mixed integers and floats

    Args:
        mxd_lst: List of integers and floats

    Returns:
        Sum of the integers and floats in the list
    """
    return sum(mxd_lst)
