#!/usr/bin/env python3
"""Multiplier"""
from typing import Callable

def make_multiplier(multiplier : float) ->  Callable[[float], float]:
    """Make Multiplier"""
    def claculate_multplier(n: float) -> float:
        """claculate_multplier"""
        return n * multiplier
    return claculate_multplier
