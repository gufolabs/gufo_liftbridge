# Gufo Liftbridge Example: Transparent Compression

We have mastered message publishing either in
the  one-by-one ([publish][publish_ex]) or
in the bulk ([bulk][bulk_ex]) approaches.
The bulk approach allows reaching much higher publishing
rate, but what to do if your messages are large?
Then we can hit the network bandwidth limitation.
*Gufo Liftbridge* offers transparent message
compression. It compresses the message before
publishing and decompresses on receiving.

!!! note
    Transparent message compression is the non-standard
    *Gufo Liftbridge* feature. It may not be compatible
    with other clients unless you manage it
    manually. Use it only when you are sure that publishers
    and subscribers are always using *Gufo Liftbridge*.

!!! note
    The stream and partition must be created before running
    the example, so refer to the [Liftbridge Docs][Liftbridge Docs] 
    or pass the [create][create] example.

``` py title="compression.py" linenums="1"
--8<-- "examples/compression.py"
```

Let's see the details. 

``` py title="compression.py" linenums="1" hl_lines="1"
--8<-- "examples/compression.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="compression.py" linenums="1" hl_lines="2"
--8<-- "examples/compression.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used.

``` py title="compression.py" linenums="1" hl_lines="4"
--8<-- "examples/compression.py"
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

``` py title="compression.py" linenums="1" hl_lines="7"
--8<-- "examples/compression.py"
```
All async code must be performed in the `async` functions,
so our `publish()` function is `async def`.

``` py title="compression.py" linenums="1" hl_lines="8 9 10"
--8<-- "examples/compression.py"
```

We need an instance of the client. The instance may be used
directly or operated as an async context manager
with the `async with` clause. When used as a context manager,
the client automatically closes all connections on the exit of context,
so its lifetime is defined explicitly. `LiftbridgeClient` requires
a list of seeds to connect the cluster, so we passed the `BROKERS` list.
Unlike the [publish][publish_ex] example we added two options:

* `compression_method`: must be `zlib` or `lzma`. Sets the algorithm
  used when message compression is requested.
* `compression_threshold`: sets the minimal size of message required
  to compress them. `0` means compressing all messages.

The client is highly configurable, refer to the
[LiftbridgeClient reference][LiftbridgeClient] for the detailed
explanations.

``` py title="compression.py" linenums="1" hl_lines="11"
--8<-- "examples/compression.py"
```

Let's publish 10 messages.

``` py title="compression.py" linenums="1" hl_lines="12 13 14 15 16 17"
--8<-- "examples/compression.py"
```

The `publish()` function is used to publish one message immediately.
The client does not enforce any specific data format and leaves
it to the application. The only requirement is to pass the message
value as the `bytes` type. In our example, we construct the string
as the message and we have to encode it to the `bytes` manually.
Then we must specify the stream and partition to publish, we use
partition `0` of stream `test` in our example.
Unlike the [publish][publish_ex] example we added `auto_compress` option.
`auto_compress` instructs the client to compress the message if it falls
beyond the threshold.

`publish()` is the async function and must be awaited. The function may accept
additional parameters, so refer to the
[publish() referece][publish] for the detailed explanations.

``` py title="compression.py" linenums="1" hl_lines="20"
--8<-- "examples/compression.py"
```
Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[publish]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.publish
[create]: create.md
[publish_ex]: publish.md
[bulk_ex]: bulk.md