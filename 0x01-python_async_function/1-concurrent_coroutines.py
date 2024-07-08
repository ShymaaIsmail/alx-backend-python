#!/usr/bin/env python3
""" Concurrent Coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait n times for random delay period"""
    routine_list = []
    delay_list = []
    for _ in range(0, n):
        routine_list.append(wait_random(max_delay))
    delay_list = await asyncio.gather(*routine_list)
    return sorted(delay_list)
