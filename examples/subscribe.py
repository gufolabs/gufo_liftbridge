import asyncio
from gufo.liftbridge.client import LiftbridgeClient, StartPosition

BROKERS = ["127.0.0.1:9292"]


async def subscribe():
    async with LiftbridgeClient(BROKERS) as client:
        async for msg in client.subscribe(
            "test", partition=0, start_position=StartPosition.EARLIEST
        ):
            print(f"{msg.offset}: {msg.value}")


asyncio.run(subscribe())
