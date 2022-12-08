import asyncio
from gufo.liftbridge.client import LiftbridgeClient, StartPosition

BROKERS = ["127.0.0.1:9292"]
CURSOR_ID = "test_cursor"


async def subscribe():
    async with LiftbridgeClient(BROKERS) as client:
        async for msg in client.subscribe(
            "test",
            partition=0,
            start_position=StartPosition.RESUME,
            cursor_id=CURSOR_ID,
        ):
            print(f"{msg.offset}: {msg.value}")
            await client.set_cursor(
                "test", partition=0, cursor_id=CURSOR_ID, offset=msg.offset
            )


asyncio.run(subscribe())
