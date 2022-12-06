# Gufo Liftbridge Example: Bulk Publishing

We have mastered the message publishing
in our [publish][publish_ex] example. Synchronous
publishing is a decent choice while the publishing
rate remains moderate. But its performance
is limited by the round-trip time (RTT).
If the server responds in 1ms, you will have
an overall limit of 1000 requests per second
for a single publisher. Bulk publishing overrides
an RTT limitation by separating request generation,
sending, and acknowledgment.

!!! note
    The stream and partition must be created before running
    the example, so refer to the [Liftbridge Docs][Liftbridge Docs] 
    or pass the [create][create_ex] example.

``` py title="bulk.py" linenums="1"
--8<-- "examples/bulk.py"
```

Let's see the details. 

``` py title="bulk.py" linenums="1" hl_lines="1"
--8<-- "examples/bulk.py"
```

*Gufo Liftbridge* is an async library. In our case
we should run the client from our synchronous script,
so we need to import `asyncio` to use `asyncio.run()`.

``` py title="bulk.py" linenums="1" hl_lines="2"
--8<-- "examples/bulk.py"
```

The client is implemented as a `LiftbridgeClient` class,
which must be imported to be used.

``` py title="bulk.py" linenums="1" hl_lines="4"
--8<-- "examples/bulk.py"
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

``` py title="bulk.py" linenums="1" hl_lines="7"
--8<-- "examples/bulk.py"
```
All async code must be performed in the `async` functions,
so our `publish()` function is `async def`.

``` py title="bulk.py" linenums="1" hl_lines="8"
--8<-- "examples/bulk.py"
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

``` py title="bulk.py" linenums="1" hl_lines="9 10 11 12 13 14"
--8<-- "examples/bulk.py"
```

We have to prepare requests for bulk publishing. In our example
we use the list comprehensions to build the list of 10 requests.
Though we use list for our example, its possible to use any
types of iterables, like generator functions and so on.

Requests are created by `get_publish_request()` method.
It accepts same parameters as the `publish()` method, but
instead of immediate publishing returns the requests
which can be passed to `publish_bulk()` later.
The client does not enforce any specific data format and leaves
it to the application. The only requirement is to pass the message
value as the `bytes` type. In our example, we construct the string
as the message and we have to encode it to the `bytes` manually.
Then we must specify the stream and partition to publish, we use
partition `0` of stream `test` in our example. It is possible
to publish into diffent streams and partition in the one
`publish_bulk()` call.

Refer to the [get_publish_request()][get_publish_request] reference
for details.

Now we're ready to publish our bulk.

``` py title="bulk.py" linenums="1" hl_lines="15 16"
--8<-- "examples/bulk.py"
```

We use `publish_bulk()` method to send our prepared bulk of requests.
The method is an asynchronous iterator, so it must be used with
`async for` directive. It sends our bulk in one or more batch
and yield the `Ack` for each request send. If the `wait` parameter
is not set, method returns just after sending the last request
and not waits for remaining acknowledgment which are in-flight.
So the amount of `for` cycle iterations may be less than lenght
of the bulk. This scenario is suitable for fire-and-forget tasks.
It is up to application to control the acknowledgments and
to deal the failures. In our example we just print them.

Refer to the [publish_bulk()][publish_bulk] reference
for details.

``` py title="bulk.py" linenums="1" hl_lines="19"
--8<-- "examples/bulk.py"
```

Use `asyncio.run()` function to start our async code.

[Liftbridge Docs]: https://liftbridge.io/docs/overview.html
[LiftbridgeClient]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient
[get_publish_request]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.get_publish_request
[publish_bulk]: ../../reference/gufo/liftbridge/client/#gufo.liftbridge.client.LiftbridgeClient.publish_bulk
[create_ex]: create.md
[publish_ex]: publish.md
