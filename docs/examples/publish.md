# Gufo Liftbridge Example: Publishing

The message queue has two fundamental operations:
publishing and subscribing. Let's write the simple
publisher. 

!!! note
    The stream and partition must be created before running
    the example, so refer to the [Liftbridge Docs][Liftbridge Docs] 
    or pass the [create][create] example.

``` py title="publish.py" linenums="1"
--8<-- "examples/publish.py"
```

Let's see the details. 

``` py title="publish.py" linenums="1" hl_lines="1"
--8<-- "examples/publish.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="publish.py" linenums="1" hl_lines="2"
--8<-- "examples/publish.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used.

``` py title="publish.py" linenums="1" hl_lines="4"
--8<-- "examples/publish.py"
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

``` py title="publish.py" linenums="1" hl_lines="7"
--8<-- "examples/publish.py"
```
All async code must be performed in the `async` functions,
so our `publish()` function is `async def`.

``` py title="publish.py" linenums="1" hl_lines="8"
--8<-- "examples/publish.py"
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

``` py title="publish.py" linenums="1" hl_lines="9"
--8<-- "examples/publish.py"
```

Let's publish 10 messages.

``` py title="publish.py" linenums="1" hl_lines="10 11 12"
--8<-- "examples/publish.py"
```

The `publish()` function is used to publish one message immediately.
The client does not enforce any specific data format and leaves
it to the application. The only requirement is to pass the message
value as the `bytes` type. In our example, we construct the string
as the message and we have to encode it to the `bytes` manually.
Then we must specify the stream and partition to publish, we use
partition `0` of stream `test` in our example.
`publish()` is the async function and must be awaited. The function may accept
additional parameters, so refer to the
[publish() referece][publish] for the detailed explanations.

``` py title="publish.py" linenums="1" hl_lines="15"
--8<-- "examples/publish.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[publish]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.publish
[create]: create.md