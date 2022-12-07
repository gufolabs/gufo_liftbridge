# ----------------------------------------------------------------------
# Gufo Liftbridge: gufo.liftbridge.client tests
# ----------------------------------------------------------------------
# Copyright (C) 2022, Gufo Labs
# See LICENSE.md for details
# ----------------------------------------------------------------------

# Python modules
import asyncio
import os
import tempfile
import subprocess


# Third-party modules
import pytest

# Gufo Liftbridge modules
from gufo.liftbridge.client import LiftbridgeClient
from gufo.liftbridge.types import StartPosition
from gufo.liftbridge.error import ErrorNotFound

LIFTBRIDGE_BIN_PATH = "/usr/local/bin/liftbridge"
LIFTBRIDGE_DATA_ROOT = "/tmp/ldata"
LIFTRIDGE_SERVER_ID = "test"
BROKER = "127.0.0.1:9292"

DEFAULT_CONFIG = """
listen: 127.0.0.1:9292
cursors:
    stream.auto.pause.time: 0
    stream.partitions: 1
"""


@pytest.fixture(scope="module")
def liftbridge():
    """
    Run and stop liftbridge process.
    """

    async def wait_for_leader():
        async with LiftbridgeClient([BROKER]) as client:
            await client.get_metadata()

    # Ensure temporary root is exists
    if not os.path.exists(LIFTBRIDGE_DATA_ROOT):
        os.makedirs(LIFTBRIDGE_DATA_ROOT)
    # Generate temporary data directory
    with tempfile.TemporaryDirectory(
        prefix="data-", dir=LIFTBRIDGE_DATA_ROOT
    ) as data_dir:
        # Write config
        cfg = os.path.join(data_dir, ".liftbridge.yml")
        with open(cfg, "w") as f:
            f.write(DEFAULT_CONFIG)
        # Launch server
        proc = subprocess.Popen(
            [
                LIFTBRIDGE_BIN_PATH,
                "-c",
                cfg,
                "-d",
                data_dir,
                "--embedded-nats",
                "--raft-bootstrap-seed",
            ],
        )
        # Wait for metadata leader
        asyncio.run(asyncio.wait_for(wait_for_leader(), 10.0))
        # Pass control to tests
        yield None
        # Stop server
        proc.kill()


def test_empty_seeds():
    with pytest.raises(ValueError):
        LiftbridgeClient([])


def test_all_broken_seeds():
    with pytest.raises(ValueError):
        LiftbridgeClient(["lorem:ipsum", "dorem:sit"])


def test_seed_resolution_failed():
    async def inner():
        async with LiftbridgeClient(["unknown.example.com:9292"]) as client:
            await client.get_metadata()

    with pytest.raises(ErrorNotFound):
        asyncio.run(inner())


@pytest.mark.parametrize(
    "v,exp",
    [
        ("127.0.0.1:1000", True),
        ("localhost:1000", True),
        ("localhost:x:1000", False),
        ("localhost:ff", False),
    ],
)
def test_is_broker_addr(v: str, exp: bool):
    assert LiftbridgeClient._is_broker_addr(v) is exp


@pytest.mark.parametrize(
    "seed,resolved", [("127.0.0.1:1000", "127.0.0.1:1000")]
)
def test_get_seed1(seed: str, resolved: str):
    async def inner():
        return await client._get_seed()

    client = LiftbridgeClient([seed])
    r = asyncio.run(inner())
    assert r == resolved


def test_get_empty_metadata(liftbridge):
    async def inner():
        async with LiftbridgeClient([BROKER]) as client:
            await client.wait_for_cursors()
            return await client.get_metadata()

    r = asyncio.run(asyncio.wait_for(inner(), 3.0))
    assert r
    nm = [m for m in r.metadata if m.name != "__cursors"]
    assert len(nm) == 0
    assert len(r.brokers) == 1
    assert r.brokers[0].host == "127.0.0.1"


def test_get_metadata(liftbridge):
    async def inner():
        async with LiftbridgeClient([BROKER]) as client:
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            r = await client.get_metadata(STREAM)
            await client.delete_stream(STREAM)
            return r

    STREAM = "test_metadata"
    r = asyncio.run(asyncio.wait_for(inner(), 20.0))
    assert r
    for m in r.metadata:
        if m.name == STREAM and len(m.partitions) == 1:
            break
    else:
        assert False, "No metadata for test stream"


def test_get_partition_metadata(liftbridge):
    async def inner():
        async with LiftbridgeClient([BROKER]) as client:
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            r = await client.get_partition_metadata(STREAM, partition=0)
            await client.delete_stream(STREAM)
            return r

    STREAM = "test_part_metadata"
    r = asyncio.run(asyncio.wait_for(inner(), 20.0))
    assert r


def test_delete_unknown_stream():
    async def inner():
        async with LiftbridgeClient([BROKER]) as client:
            await client.delete_stream("_unknown_stream")

    with pytest.raises(ErrorNotFound):
        asyncio.run(asyncio.wait_for(inner(), 20.0))


def test_pub_sub():
    async def prepare_stream():
        print("[prep] Running")
        async with LiftbridgeClient([BROKER]) as client:
            print("[prep] Crearing stream")
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            print("[prep] Stream is ready")
            prep_ready.set()
            print("[prep] Waiting for publisher")
            await pub_ready.wait()
            print("[prep] Waiting for subscriber")
            await sub_ready.wait()
            print("[prep] Done")

    async def publisher():
        print("[pub] Running")
        await prep_ready.wait()
        async with LiftbridgeClient([BROKER]) as client:
            print("[pub] Starting publishing")
            for i in range(N):
                print(f"[pub] Publishing #{i}")
                await client.publish(
                    f"msg{i}".encode("utf-8"),
                    stream=STREAM,
                    partition=0,
                    headers={"test": f"n{i}".encode("utf-8")},
                )
        print("[pub] Finishing")
        pub_ready.set()
        print("[pub] Done")

    async def subscriber():
        print("[sub] Running")
        await prep_ready.wait()
        expected = 0
        async with LiftbridgeClient([BROKER]) as client:
            print("[sub] Subscribing")
            async for msg in client.subscribe(
                STREAM, partition=0, start_position=StartPosition.EARLIEST
            ):
                print(f"[sub] Received #{msg.offset}")
                assert msg.offset == expected
                assert msg.value == f"msg{expected}".encode("utf-8")
                assert "test" in msg.headers
                assert msg.headers["test"] == f"n{expected}".encode("utf-8")
                expected += 1
                if expected == N:
                    break
        print("[sub] Finising")
        sub_ready.set()
        print("[sub] Done")

    async def run():
        await asyncio.gather(
            prepare_stream(),
            publisher(),
            subscriber(),
        )

    STREAM = "test_pubsub1"
    N = 10
    prep_ready = asyncio.Event()
    sub_ready = asyncio.Event()
    pub_ready = asyncio.Event()
    asyncio.run(asyncio.wait_for(run(), 10.0))


def test_pub_sub_offset():
    async def prepare_stream():
        print("[prep] Running")
        async with LiftbridgeClient([BROKER]) as client:
            print("[prep] Crearing stream")
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            print("[prep] Stream is ready")
            prep_ready.set()
            print("[prep] Waiting for publisher")
            await pub_ready.wait()
            print("[prep] Waiting for subscriber")
            await sub_ready.wait()
            print("[prep] Done")

    async def publisher():
        print("[pub] Running")
        await prep_ready.wait()
        async with LiftbridgeClient([BROKER]) as client:
            print("[pub] Starting publishing")
            for i in range(N):
                print(f"[pub] Publishing #{i}")
                await client.publish(
                    f"msg{i}".encode("utf-8"),
                    stream=STREAM,
                    partition=0,
                    headers={"test": f"n{i}".encode("utf-8")},
                )
        print("[pub] Finishing")
        pub_ready.set()
        print("[pub] Done")

    async def subscriber():
        print("[sub] Running")
        await pub_ready.wait()
        expected = 5
        async with LiftbridgeClient([BROKER]) as client:
            print("[sub] Subscribing")
            async for msg in client.subscribe(
                STREAM, partition=0, start_offset=5
            ):
                print(f"[sub] Received #{msg.offset}")
                assert msg.offset == expected
                assert msg.value == f"msg{expected}".encode("utf-8")
                assert "test" in msg.headers
                assert msg.headers["test"] == f"n{expected}".encode("utf-8")
                expected += 1
                if expected == N:
                    break
        print("[sub] Finising")
        sub_ready.set()
        print("[sub] Done")

    async def run():
        await asyncio.gather(
            prepare_stream(),
            publisher(),
            subscriber(),
        )

    STREAM = "test_pubsub3"
    N = 10
    prep_ready = asyncio.Event()
    sub_ready = asyncio.Event()
    pub_ready = asyncio.Event()
    asyncio.run(asyncio.wait_for(run(), 10.0))


def test_pub_sub_resume():
    async def prepare_stream():
        print("[prep] Running")
        async with LiftbridgeClient([BROKER]) as client:
            print("[prep] Crearing stream")
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            print("[prep] Stream is ready")
            prep_ready.set()
            print("[prep] Waiting for publisher")
            await pub_ready.wait()
            print("[prep] Waiting for subscriber")
            await sub_ready.wait()
            print("[prep] Done")

    async def publisher():
        print("[pub] Running")
        await prep_ready.wait()
        async with LiftbridgeClient([BROKER]) as client:
            print("[pub] Starting publishing")
            for i in range(N):
                print(f"[pub] Publishing #{i}")
                await client.publish(
                    f"msg{i}".encode("utf-8"),
                    stream=STREAM,
                    partition=0,
                    headers={"test": f"n{i}".encode("utf-8")},
                )
        print("[pub] Set cursor")
        await client.set_cursor(
            STREAM, partition=0, cursor_id=CURSOR, offset=4
        )
        print("[pub] Finishing")
        pub_ready.set()
        print("[pub] Done")

    async def subscriber():
        print("[sub] Running")
        await pub_ready.wait()
        expected = 5
        async with LiftbridgeClient([BROKER]) as client:
            print("[sub] Subscribing")
            async for msg in client.subscribe(
                STREAM,
                partition=0,
                start_position=StartPosition.RESUME,
                cursor_id=CURSOR,
            ):
                print(f"[sub] Received #{msg.offset}")
                assert msg.offset == expected
                assert msg.value == f"msg{expected}".encode("utf-8")
                assert "test" in msg.headers
                assert msg.headers["test"] == f"n{expected}".encode("utf-8")
                expected += 1
                if expected == N:
                    break
        print("[sub] Finising")
        sub_ready.set()
        print("[sub] Done")

    async def run():
        await asyncio.gather(
            prepare_stream(),
            publisher(),
            subscriber(),
        )

    STREAM = "test_pubsub4"
    CURSOR = "pos"
    N = 10
    prep_ready = asyncio.Event()
    sub_ready = asyncio.Event()
    pub_ready = asyncio.Event()
    asyncio.run(asyncio.wait_for(run(), 10.0))


def test_bulk_pub_sub():
    async def prepare_stream():
        print("[prep] Running")
        async with LiftbridgeClient([BROKER]) as client:
            print("[prep] Crearing stream")
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            print("[prep] Stream is ready")
            prep_ready.set()
            print("[prep] Waiting for publisher")
            await pub_ready.wait()
            print("[prep] Waiting for subscriber")
            await sub_ready.wait()
            print("[prep] Done")

    def pub_iter():
        client = LiftbridgeClient([BROKER], compression_method="lzma")
        for i in range(N):
            yield client.get_publish_request(
                f"msg{i}".encode("utf-8"),
                stream=STREAM,
                partition=0,
                headers={"test": f"n{i}".encode("utf-8")},
                key=f"{i}".encode("utf-8"),
                correlation_id="test-run",
                auto_compress=True,
            )

    async def publisher():
        print("[pub] Running")
        await prep_ready.wait()
        async with LiftbridgeClient([BROKER]) as client:
            print("[pub] Starting publishing")
            async for _ in client.publish_bulk(pub_iter()):
                pass
        print("[pub] Finishing")
        pub_ready.set()
        print("[pub] Done")

    async def subscriber():
        print("[sub] Running")
        await prep_ready.wait()
        expected = 0
        async with LiftbridgeClient([BROKER]) as client:
            print("[sub] Subscribing")
            async for msg in client.subscribe(
                STREAM, partition=0, start_position=StartPosition.EARLIEST
            ):
                print(f"[sub] Received #{msg.offset}")
                assert msg.offset == expected
                assert msg.value == f"msg{expected}".encode("utf-8")
                assert "test" in msg.headers
                assert msg.headers["test"] == f"n{expected}".encode("utf-8")
                expected += 1
                if expected == N:
                    break
        print("[sub] Finising")
        sub_ready.set()
        print("[sub] Done")

    async def run():
        await asyncio.gather(
            prepare_stream(),
            publisher(),
            subscriber(),
        )

    STREAM = "test_pubsub2"
    N = 10
    prep_ready = asyncio.Event()
    sub_ready = asyncio.Event()
    pub_ready = asyncio.Event()
    asyncio.run(asyncio.wait_for(run(), 10.0))


def test_cursor():
    async def prepare_stream():
        print("[prep] Running")
        async with LiftbridgeClient([BROKER]) as client:
            print("[prep] Crearing stream")
            await client.create_stream(
                STREAM, partitions=1, wait_for_stream=True
            )
            print("[prep] Stream is ready")
            await client.wait_for_cursors()
            print("[prep] Cursors stream is ready")
            prep_ready.set()
            print("[prep] Waiting for cursors")
            await cur_ready.wait()
            print("[prep] Done")

    async def cursors():
        print("[cur] Running")
        await prep_ready.wait()
        async with LiftbridgeClient([BROKER]) as client:
            # Empty cursor
            print("[cur] Getting empty cursor")
            c = await client.get_cursor(STREAM, partition=0, cursor_id=CURSOR)
            print(f"[cur] Empty cursor is {c}")
            assert c == -1
            #
            for i in range(N):
                print(f"[cur] Setting cursor to {i}")
                await client.set_cursor(
                    STREAM, partition=0, cursor_id=CURSOR, offset=i
                )
                print("[cur] Getting cursor")
                c = await client.get_cursor(
                    STREAM, partition=0, cursor_id=CURSOR
                )
                print(f"[cur] Got {c}")
                assert c == i + 1
        cur_ready.set()
        print("[cur] Done")

    async def run():
        await asyncio.gather(
            prepare_stream(),
            cursors(),
        )

    STREAM = "test_cursor"
    CURSOR = "test"
    N = 10
    prep_ready = asyncio.Event()
    cur_ready = asyncio.Event()
    asyncio.run(asyncio.wait_for(run(), 10.0))


@pytest.mark.parametrize("name,exp", [("localhost", "127.0.0.1")])
def test_resolve(name: str, exp: str, liftbridge):
    async def inner():
        async with LiftbridgeClient([BROKER]) as client:
            return await client._resolve(name, cache)

    cache = {}
    r = asyncio.run(inner())
    assert r == exp
    assert name in cache
    assert cache[name][0] == exp
