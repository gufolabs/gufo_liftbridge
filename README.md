# Gufo Liftbridge

*An asynchronous [Python][Python] [Liftbridge][Liftbridge] client*

[![PyPi version](https://img.shields.io/pypi/v/gufo_liftbridge.svg)](https://pypi.python.org/pypi/gufo_liftbridge/)
![Python Versions](https://img.shields.io/pypi/pyversions/gufo_liftbridge)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![Build](https://img.shields.io/github/workflow/status/gufolabs/gufo_liftbridge/Run%20Tests/master)
![Sponsors](https://img.shields.io/github/sponsors/gufolabs)

---

**Documentation**: [https://docs.gufolabs.com/gufo_liftbridge/](https://docs.gufolabs.com/gufo_liftbridge/)

**Source Code**: [https://github.com/gufolabs/gufo_liftbridge/](https://github.com/gufolabs/gufo_liftbridge/)

---

*Gufo Liftbridge* is the Python asyncio Liftbridge client library. It hides complex cluster
topology management handling tasks and the internals of the gRPC as well. Client offers
following features:

* Publishing.
* Subscribing.
* Bulk publishing.
* Cursors manipulation.
* Cluster metadata fetching.
* Stream creating and destroying.
* Transparent data compression (own extension, may be not compatible with other clients).

## Installing

```
pip install gufo_liftbridge
```

## Publishing

``` python
from gufo.liftbridge.client import LiftbridgeClient

async def publish():
    async with LiftbridgeClient(["127.0.0.1:9292"]) as client:
        await client.publish(b"mybinarydata", stream="test", partition=0)
```

## Subscribing

``` python
from gufo.liftbridge.client import LiftbridgeClient

async def subscribe():
    async with LiftbridgeClient(["127.0.0.1:9292"]) as client:
        async for msg in client.subscribe("test", partition=0):
            print(f"{msg.offset}: {msg.value}")
```

## Virtues

* Clean async API.
* High-performance.
* Full Python typing support.
* Editor completion.
* Well-tested, battle-proven code.

[Python]: https://python.org/
[Liftbridge]: https://liftbridge.io/