import asyncio
from gufo.liftbridge.client import LiftbridgeClient

BROKERS = ["127.0.0.1:9292"]


async def create():
    async with LiftbridgeClient(BROKERS) as client:
        await client.create_stream("test", partitions=1, wait_for_stream=True)


asyncio.run(create())
