# Gufo Liftbridge Example: Subscribing

We have mastered the message publishing process
in our [publish][publish_ex] example. We also
learned about various optimizations from
[bulk][bulk_ex] and [compression][compression_ex].
Now it is a time to learn about
receiving messages. To get published messages
we need to subscribe to the stream.

!!! note
    The stream and partition must be created before running
    the example, so refer to the [Liftbridge Docs][Liftbridge Docs] 
    or pass the [create][create_ex] example.

``` py title="subscribe.py" linenums="1"
--8<-- "examples/subscribe.py"
```

Let's see the details. 

``` py title="subscribe.py" linenums="1" hl_lines="1"
--8<-- "examples/subscribe.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="subscribe.py" linenums="1" hl_lines="2"
--8<-- "examples/subscribe.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used. We also need the
`StartPosition` enum.

``` py title="subscribe.py" linenums="1" hl_lines="4"
--8<-- "examples/subscribe.py"
```
Liftbridge is the dynamic cluster, synchronized over
Raft protocol. Cluster members may enter and leave and
the client uses one or more cluster members as a bootstrap
to recover an actual topology. These bootstrap
members are called `seeds` and are defined as a list
of the strings in the `host:port` format. For our
example, we consider the Liftbridge is running
locally at the `127.0.0.1:9292`. Take note, ever we have
one seed, we must define it as a list.

``` py title="subscribe.py" linenums="1" hl_lines="7"
--8<-- "examples/subscribe.py"
```
All async code must be performed in the `async` functions,
so our `subscribe()` function is `async def`.

``` py title="subscribe.py" linenums="1" hl_lines="8"
--8<-- "examples/subscribe.py"
```

We need an instance of the client. The instance may be used
directly or operated as an async context manager
with the `async with` clause. When used as a context manager,
the client automatically closes all connections on the exit of context,
so its lifetime is defined explicitly. `LiftbridgeClient` requires
a list of seeds to connect the cluster, so we passed the `BROKERS` list.
The client is highly configurable, refer to the
[LiftbridgeClient reference][LiftbridgeClient] for the detailed
explanations.

``` py title="subscribe.py" linenums="1" hl_lines="9 10 11"
--8<-- "examples/subscribe.py"
```

The `subscribe()` method is used to receive the messages. We need to
pass the stream (`test`), the partition (`0`), and the position
from which to start receiving the messages. In our case, we
use `StartPosition.EARLIEST` to receive all the messages
still stored in the stream. To learn about other starting
options refer to [StartPosition][StartPosition] documentation.

The client implements subscribing as an async iterator, so
the `async for` operator is usually used to iterate through.
The result of iteration is the [Message][Message] structure.
The cycle is endless so it is up to the application to decide
whenever to do the `break`.

For additional parameters refer to the [subscribe][subscribe]
documentation.

``` py title="subscribe.py" linenums="1" hl_lines="12"
--8<-- "examples/subscribe.py"
```

All following processing is built around the [Message][Message]
structure. It consists of several fields. Message body contained
in the `value` attribute. The body is the raw `bytes` type
and it's up to the application to handle them properly.
We just use  `print()` to display the message body as well as
the message's sequential number in the partition from the `offset`
attribute.

``` py title="subscribe.py" linenums="1" hl_lines="15"
--8<-- "examples/subscribe.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[subscribe]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.subscribe
[StartPosition]: ../../reference/gufo/liftbridge/types/#gufo.liftbridge.types.StartPosition
[Message]: ../../reference/gufo/liftbridge/types/#gufo.liftbridge.types.Message
[create_ex]: create.md
[publish_ex]: publish.md
[bulk_ex]: bulk.md
[compression_ex]: compression.md