# Gufo Liftbridge Example: Create Stream

The Liftridge's streams and partitions
must be created before usage. Let's create
the stream via LiftridgeClient.


``` py title="create.py" linenums="1"
--8<-- "examples/create.py"
```

Let's see the details. 

``` py title="create.py" linenums="1" hl_lines="1"
--8<-- "examples/create.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="create.py" linenums="1" hl_lines="2"
--8<-- "examples/create.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used.

``` py title="create.py" linenums="1" hl_lines="4"
--8<-- "examples/create.py"
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

``` py title="create.py" linenums="1" hl_lines="7"
--8<-- "examples/create.py"
```
All async code must be performed in the `async` functions,
so our `create()` function is `async def`.

``` py title="create.py" linenums="1" hl_lines="8"
--8<-- "examples/create.py"
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

``` py title="create.py" linenums="1" hl_lines="9"
--8<-- "examples/create.py"
```

We use the [create_stream()][create] function to create
a stream `test` with one partition. By default, [create_stream()][create]
doesn't wait until the partition is replicated via the cluster.
The `wait_for_stream` parameter instructs to wait until the new stream
is ready for use. The [create_stream()][create] is an async function
and must be awaited.

Refer to the [create_stream()][create] reference for the explanations.

``` py title="create.py" linenums="1" hl_lines="12"
--8<-- "examples/create.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[create_stream]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.create_stream
[create]: create.md