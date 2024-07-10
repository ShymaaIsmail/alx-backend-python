#!/usr/bin/env python3
"""Async Generator Comprehension"""
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """async_comprehension"""
    return [i async for i in async_generator()]
