# Gufo Liftbridge Example: Delete Stream

We have mastered the stream creation process
in our [create][create_ex] example. Now we'll
learn how to delete a stream.


``` py title="delete.py" linenums="1"
--8<-- "examples/delete.py"
```

Let's see the details. 

``` py title="delete.py" linenums="1" hl_lines="1"
--8<-- "examples/delete.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="delete.py" linenums="1" hl_lines="2"
--8<-- "examples/delete.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used.

``` py title="delete.py" linenums="1" hl_lines="4"
--8<-- "examples/delete.py"
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

``` py title="delete.py" linenums="1" hl_lines="7"
--8<-- "examples/delete.py"
```
All async code must be performed in the `async` functions,
so our `delete()` function is `async def`.

``` py title="delete.py" linenums="1" hl_lines="8"
--8<-- "examples/delete.py"
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

``` py title="delete.py" linenums="1" hl_lines="9"
--8<-- "examples/delete.py"
```

We use the [delete_stream()][delete_stream] function to delete the `test` stream
and all its partitions. The [delete_stream()][delete_stream] is an async function
and must be awaited.

``` py title="delete.py" linenums="1" hl_lines="12"
--8<-- "examples/delete.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[delete_stream]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.delete_stream
[create_ex]: create.md