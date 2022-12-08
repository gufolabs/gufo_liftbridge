import asyncio
from gufo.liftbridge.client import LiftbridgeClient

BROKERS = ["127.0.0.1:9292"]


async def delete():
    async with LiftbridgeClient(BROKERS) as client:
        await client.delete_stream("test")


asyncio.run(delete())
