import pytest

from vvclient import Client


@pytest.mark.asyncio
async def test_basic():
    async with Client() as client:
        await client.init_speaker(1)
        assert await client.is_inited_speaker(1)
