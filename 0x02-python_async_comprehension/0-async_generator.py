#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator"""
    for _ in range(10):
        random_float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_float
