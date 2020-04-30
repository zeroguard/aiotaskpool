"""Test all placeholder."""
import pytest
import random
import asyncio

from aiotaskpool import TaskPool


async def wait_and_echo(item):
    rand = random.random()
    await asyncio.sleep(rand)
    return rand


@pytest.mark.asyncio
async def test_placeholder():
    """."""
    items = range(10)
    task_pool = TaskPool(32)
    async with task_pool.map(wait_and_echo, items) as results:
        results.stats.enable()
        async for result in results:
            assert result
