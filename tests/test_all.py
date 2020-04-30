"""Test all placeholder."""
import asyncio
import pytest
import random

from aiotaskpool import TaskPool

async def random_wait(idx):
    i = random.random()
    await asyncio.sleep(i)
    return i


@pytest.mark.asyncio
async def test_all():
    """."""
    items = range(100_000)
    tp = TaskPool(32)
    async with tp.map(random_wait, items) as results:
        async for result in results:
            pass#print(result)
