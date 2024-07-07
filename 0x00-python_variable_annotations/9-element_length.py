#!/usr/bin/env python3
""" Element Length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element Length"""
    return [(i, len(i)) for i in lst]
