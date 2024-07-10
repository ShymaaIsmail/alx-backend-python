#!/usr/bin/env python3
"""Measure Time"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start_time = time.perf_counter()
    routine_list = []
    for _ in range(0, 4):
        routine_list.append(async_comprehension())
    await asyncio.gather(*routine_list)
    elapsed = time.perf_counter() - start_time
    return elapsed
