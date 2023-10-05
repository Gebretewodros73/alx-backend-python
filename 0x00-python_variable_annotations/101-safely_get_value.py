#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary
"""


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value associated with the
    given key in the dictionary,
    or the default value if the key is not present.

    Args:
        dct: A mapping (e.g., dictionary).
        key: The key to look up.
        default: The value to return if
        the key is not present. Defaults to None.

    Returns:
        The value associated with the key,
        or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
