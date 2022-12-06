import asyncio
from gufo.liftbridge.client import LiftbridgeClient

BROKERS = ["127.0.0.1:9292"]


async def publish():
    async with LiftbridgeClient(BROKERS) as client:
        bulk = [
            client.get_publish_request(
                f"msg{i}".encode("utf-8"), stream="test", partition=0
            )
            for i in range(10)
        ]
        async for ack in client.publish_bulk(bulk, wait=True):
            print(ack)


asyncio.run(publish())
