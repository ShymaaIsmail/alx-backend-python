#!/usr/bin/env python3
""" Convert to key and value"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Convert to key and value"""
    return (k, v ** 2)
