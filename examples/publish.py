import asyncio
from gufo.liftbridge.client import LiftbridgeClient

BROKERS = ["127.0.0.1:9292"]


async def publish():
    async with LiftbridgeClient(BROKERS) as client:
        for i in range(10):
            await client.publish(
                f"msg{i}".encode("utf-8"), stream="test", partition=0
            )


asyncio.run(publish())
