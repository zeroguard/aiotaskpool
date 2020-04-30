"""Test all placeholder."""
import asyncio
import pytest
import random

from aiotaskpool import TaskPool


async def random_wait(idx):
    """."""
    i = random.random()
    await asyncio.sleep(i)
    return i


@pytest.mark.asyncio
async def test_imap():
    """."""
    items = range(1000)
    task_pool = TaskPool(32)
    async with task_pool.imap(random_wait, items) as results:
        async for result in results:
            print(result.args, result.result())


@pytest.mark.asyncio
async def test_map():
    """."""
    items = range(1000)
    task_pool = TaskPool(32)
    results = await task_pool.map(random_wait, items)
    for result in results:
        print(result.args, result.result())
