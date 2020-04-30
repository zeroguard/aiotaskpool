#!/usr/bin/env python3
"""Test all placeholder."""
import asyncio
import random

from aiotaskpool import TaskPool

################

async def random_wait(idx):
    i = random.random()
    await asyncio.sleep(i)
    return i


async def test_all():
    """."""
    items = list(range(100_000))
    tp = TaskPool(1024)
    async with tp.map(random_wait, items) as results:
        async for result in results:
            print(result.args, result.result())


async def random_wait_loop():
    while True:
        i = random.random()
        await asyncio.sleep(i)


async def test_all2():
    """."""
    tasks = []
    for x in range(1024):
        t = asyncio.create_task(random_wait_loop())
        tasks += [t]

    await asyncio.gather(*tasks)


asyncio.run(test_all())
