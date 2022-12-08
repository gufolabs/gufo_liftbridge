# Gufo Liftbridge Example: Subscribing with Cursor

We have mastered the message subscription process
in our [subscribe][subscribe_ex] example. We processed
all the messages still stored in the partition. But what
to do if the subscriber is restartable and we need to
start from the first unprocessed message? Surely, we need
to save the current position somewhere. It's up to the application
where to store the position. In our example,
we will use Liftbridge's cursors, the dedicated position storage
just inside the Liftbridge  database.

!!! note
    The stream and partition must be created before running
    the example, so refer to the [Liftbridge Docs][Liftbridge Docs] 
    or pass the [create][create_ex] example.

``` py title="subcursor.py" linenums="1"
--8<-- "examples/subcursor.py"
```

Let's see the details. 

``` py title="subcursor.py" linenums="1" hl_lines="1"
--8<-- "examples/subcursor.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="subcursor.py" linenums="1" hl_lines="2"
--8<-- "examples/subcursor.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used. We also need the
`StartPosition` enum.

``` py title="subcursor.py" linenums="1" hl_lines="4"
--8<-- "examples/subcursor.py"
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

``` py title="subcursor.py" linenums="1" hl_lines="5"
--8<-- "examples/subcursor.py"
```

Various subscribers may process the same partition in the same
time, so multiple cursors on partition may exist.
Each cursor has its own id. We use `test_cursor`
for our example.

``` py title="subcursor.py" linenums="1" hl_lines="8"
--8<-- "examples/subcursor.py"
```
All async code must be performed in the `async` functions,
so our `subscribe()` function is `async def`.

``` py title="subcursor.py" linenums="1" hl_lines="9"
--8<-- "examples/subcursor.py"
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

``` py title="subcursor.py" linenums="1" hl_lines="10 11 12 13 14 15"
--8<-- "examples/subcursor.py"
```

The `subscribe()` method is used to receive the messages. We need to
pass the stream (`test`), the partition (`0`), and the position
from which to start receiving the messages. In our case, we
use `StartPosition.RESUMEE` to resume the last position, 
stored in the cursor.
The cursor's id must be passed as the `cursor_id` parameter.

The client implements subscribing as an async iterator, so
the `async for` operator is usually used to iterate through.
The result of iteration is the [Message][Message] structure.
The cycle is endless so it is up to the application to decide
whenever to do the `break`.

For additional parameters refer to the [subscribe][subscribe]
documentation.

``` py title="subcursor.py" linenums="1" hl_lines="16"
--8<-- "examples/subcursor.py"
```

All following processing is built around the [Message][Message]
structure. It consists of several fields. Message body contained
in the `value` attribute. The body is the raw `bytes` type
and it's up to the application to handle them properly.
We just use  `print()` to display the message body as well as
the message's sequential number in the partition from the `offset`
attribute.

``` py title="subcursor.py" linenums="1" hl_lines="17 18 19"
--8<-- "examples/subcursor.py"
```

After we processed the message we must store the message's
offset into the cursor. `set_cursor` accepts the following parameters:

* `stream`: The stream name.
* `partition`: The partition.
* `cursor_id`: The cursor's id.
* `offset`: The current message offset.

The function is asynchronous and must be awaited.

``` py title="subcursor.py" linenums="1" hl_lines="22"
--8<-- "examples/subcursor.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[subscribe]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.subscribe
[StartPosition]: ../../reference/gufo/liftbridge/types/#gufo.liftbridge.types.StartPosition
[Message]: ../../reference/gufo/liftbridge/types/#gufo.liftbridge.types.Message
[create_ex]: create.md
[subscribe_ex]: subscribe.md
[bulk_ex]: bulk.md
[compression_ex]: compression.md