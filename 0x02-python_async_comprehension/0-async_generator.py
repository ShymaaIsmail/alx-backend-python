#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def async_generator():
    """async_generator"""
    for _ in range(10):
        random_float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_float
