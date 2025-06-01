#!/usr/bin/env python3
"""Utility functions for accessing nested maps, fetching JSON data, and memoization."""

from typing import Any, Mapping, Sequence
import requests
from functools import wraps

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Accesses a value in a nested map using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

def get_json(url: str) -> dict:
    """Fetches JSON data from a given URL."""
    response = requests.get(url)
    return response.json()

def memoize(func):
    """Decorator to cache function outputs based on input arguments."""
    cache = {}

    @wraps(func)
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized
