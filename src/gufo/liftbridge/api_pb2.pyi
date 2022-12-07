from typing import List
from google.protobuf.internal import (  # type:ignore[import]
    containers as _containers,
)
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor  # type:ignore[import]
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

ALL: AckPolicy
CREATE_STREAM: ActivityStreamOp
DELETE_STREAM: ActivityStreamOp
DESCRIPTOR: _descriptor.FileDescriptor
EARLIEST: StartPosition
JOIN_CONSUMER_GROUP: ActivityStreamOp
LATEST: StartPosition
LEADER: AckPolicy
LEAVE_CONSUMER_GROUP: ActivityStreamOp
NEW_ONLY: StartPosition
NONE: AckPolicy
OFFSET: StartPosition
PAUSE_STREAM: ActivityStreamOp
RESUME_STREAM: ActivityStreamOp
SET_STREAM_READONLY: ActivityStreamOp
STOP_LATEST: StopPosition
STOP_OFFSET: StopPosition
STOP_ON_CANCEL: StopPosition
STOP_TIMESTAMP: StopPosition
TIMESTAMP: StartPosition

class Ack(_message.Message):
    __slots__ = [
        "ackError",
        "ackInbox",
        "ackPolicy",
        "commitTimestamp",
        "correlationId",
        "msgSubject",
        "offset",
        "partitionSubject",
        "receptionTimestamp",
        "stream",
    ]

    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__: List[str] = []
    ACKERROR_FIELD_NUMBER: _ClassVar[int]
    ACKINBOX_FIELD_NUMBER: _ClassVar[int]
    ACKPOLICY_FIELD_NUMBER: _ClassVar[int]
    COMMITTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION: Ack.Error
    INCORRECT_OFFSET: Ack.Error
    MSGSUBJECT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    OK: Ack.Error
    PARTITIONSUBJECT_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    TOO_LARGE: Ack.Error
    UNKNOWN: Ack.Error
    ackError: Ack.Error
    ackInbox: str
    ackPolicy: AckPolicy
    commitTimestamp: int
    correlationId: str
    msgSubject: str
    offset: int
    partitionSubject: str
    receptionTimestamp: int
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitionSubject: _Optional[str] = ...,
        msgSubject: _Optional[str] = ...,
        offset: _Optional[int] = ...,
        ackInbox: _Optional[str] = ...,
        correlationId: _Optional[str] = ...,
        ackPolicy: _Optional[_Union[AckPolicy, str]] = ...,
        receptionTimestamp: _Optional[int] = ...,
        commitTimestamp: _Optional[int] = ...,
        ackError: _Optional[_Union[Ack.Error, str]] = ...,
    ) -> None: ...

class ActivityStreamEvent(_message.Message):
    __slots__ = [
        "createStreamOp",
        "deleteStreamOp",
        "id",
        "joinConsumerGroupOp",
        "leaveConsumerGroupOp",
        "op",
        "pauseStreamOp",
        "resumeStreamOp",
        "setStreamReadonlyOp",
    ]
    CREATESTREAMOP_FIELD_NUMBER: _ClassVar[int]
    DELETESTREAMOP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JOINCONSUMERGROUPOP_FIELD_NUMBER: _ClassVar[int]
    LEAVECONSUMERGROUPOP_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    PAUSESTREAMOP_FIELD_NUMBER: _ClassVar[int]
    RESUMESTREAMOP_FIELD_NUMBER: _ClassVar[int]
    SETSTREAMREADONLYOP_FIELD_NUMBER: _ClassVar[int]
    createStreamOp: CreateStreamOp
    deleteStreamOp: DeleteStreamOp
    id: int
    joinConsumerGroupOp: JoinConsumerGroupOp
    leaveConsumerGroupOp: LeaveConsumerGroupOp
    op: ActivityStreamOp
    pauseStreamOp: PauseStreamOp
    resumeStreamOp: ResumeStreamOp
    setStreamReadonlyOp: SetStreamReadonlyOp
    def __init__(
        self,
        id: _Optional[int] = ...,
        op: _Optional[_Union[ActivityStreamOp, str]] = ...,
        createStreamOp: _Optional[_Union[CreateStreamOp, _Mapping]] = ...,
        deleteStreamOp: _Optional[_Union[DeleteStreamOp, _Mapping]] = ...,
        pauseStreamOp: _Optional[_Union[PauseStreamOp, _Mapping]] = ...,
        resumeStreamOp: _Optional[_Union[ResumeStreamOp, _Mapping]] = ...,
        setStreamReadonlyOp: _Optional[
            _Union[SetStreamReadonlyOp, _Mapping]
        ] = ...,
        joinConsumerGroupOp: _Optional[
            _Union[JoinConsumerGroupOp, _Mapping]
        ] = ...,
        leaveConsumerGroupOp: _Optional[
            _Union[LeaveConsumerGroupOp, _Mapping]
        ] = ...,
    ) -> None: ...

class Broker(_message.Message):
    __slots__ = ["host", "id", "leaderCount", "partitionCount", "port"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEADERCOUNT_FIELD_NUMBER: _ClassVar[int]
    PARTITIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    id: str
    leaderCount: int
    partitionCount: int
    port: int
    def __init__(
        self,
        id: _Optional[str] = ...,
        host: _Optional[str] = ...,
        port: _Optional[int] = ...,
        partitionCount: _Optional[int] = ...,
        leaderCount: _Optional[int] = ...,
    ) -> None: ...

class Consumer(_message.Message):
    __slots__ = ["consumerId", "groupEpoch", "groupId"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    GROUPEPOCH_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    groupEpoch: int
    groupId: str
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        groupEpoch: _Optional[int] = ...,
        consumerId: _Optional[str] = ...,
    ) -> None: ...

class ConsumerGroupMetadata(_message.Message):
    __slots__ = ["coordinator", "epoch", "error", "groupId"]

    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__: List[str] = []
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    OK: ConsumerGroupMetadata.Error
    UNKNOWN_GROUP: ConsumerGroupMetadata.Error
    coordinator: str
    epoch: int
    error: ConsumerGroupMetadata.Error
    groupId: str
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        error: _Optional[_Union[ConsumerGroupMetadata.Error, str]] = ...,
        coordinator: _Optional[str] = ...,
        epoch: _Optional[int] = ...,
    ) -> None: ...

class CreateStreamOp(_message.Message):
    __slots__ = ["partitions", "stream"]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class CreateStreamRequest(_message.Message):
    __slots__ = [
        "autoPauseDisableIfSubscribers",
        "autoPauseTime",
        "cleanerInterval",
        "compactEnabled",
        "compactMaxGoroutines",
        "encryption",
        "group",
        "minIsr",
        "name",
        "optimisticConcurrencyControl",
        "partitions",
        "replicationFactor",
        "retentionMaxAge",
        "retentionMaxBytes",
        "retentionMaxMessages",
        "segmentMaxAge",
        "segmentMaxBytes",
        "subject",
    ]
    AUTOPAUSEDISABLEIFSUBSCRIBERS_FIELD_NUMBER: _ClassVar[int]
    AUTOPAUSETIME_FIELD_NUMBER: _ClassVar[int]
    CLEANERINTERVAL_FIELD_NUMBER: _ClassVar[int]
    COMPACTENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPACTMAXGOROUTINES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MINISR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIMISTICCONCURRENCYCONTROL_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    REPLICATIONFACTOR_FIELD_NUMBER: _ClassVar[int]
    RETENTIONMAXAGE_FIELD_NUMBER: _ClassVar[int]
    RETENTIONMAXBYTES_FIELD_NUMBER: _ClassVar[int]
    RETENTIONMAXMESSAGES_FIELD_NUMBER: _ClassVar[int]
    SEGMENTMAXAGE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTMAXBYTES_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    autoPauseDisableIfSubscribers: NullableBool
    autoPauseTime: NullableInt64
    cleanerInterval: NullableInt64
    compactEnabled: NullableBool
    compactMaxGoroutines: NullableInt32
    encryption: NullableBool
    group: str
    minIsr: NullableInt32
    name: str
    optimisticConcurrencyControl: NullableBool
    partitions: int
    replicationFactor: int
    retentionMaxAge: NullableInt64
    retentionMaxBytes: NullableInt64
    retentionMaxMessages: NullableInt64
    segmentMaxAge: NullableInt64
    segmentMaxBytes: NullableInt64
    subject: str
    def __init__(
        self,
        subject: _Optional[str] = ...,
        name: _Optional[str] = ...,
        group: _Optional[str] = ...,
        replicationFactor: _Optional[int] = ...,
        partitions: _Optional[int] = ...,
        retentionMaxBytes: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        retentionMaxMessages: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        retentionMaxAge: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        cleanerInterval: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        segmentMaxBytes: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        segmentMaxAge: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        compactMaxGoroutines: _Optional[_Union[NullableInt32, _Mapping]] = ...,
        compactEnabled: _Optional[_Union[NullableBool, _Mapping]] = ...,
        autoPauseTime: _Optional[_Union[NullableInt64, _Mapping]] = ...,
        autoPauseDisableIfSubscribers: _Optional[
            _Union[NullableBool, _Mapping]
        ] = ...,
        minIsr: _Optional[_Union[NullableInt32, _Mapping]] = ...,
        optimisticConcurrencyControl: _Optional[
            _Union[NullableBool, _Mapping]
        ] = ...,
        encryption: _Optional[_Union[NullableBool, _Mapping]] = ...,
    ) -> None: ...

class CreateStreamResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class DeleteStreamOp(_message.Message):
    __slots__ = ["stream"]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    stream: str
    def __init__(self, stream: _Optional[str] = ...) -> None: ...

class DeleteStreamRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteStreamResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class FetchConsumerGroupAssignmentsRequest(_message.Message):
    __slots__ = ["consumerId", "epoch", "groupId"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    epoch: int
    groupId: str
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        consumerId: _Optional[str] = ...,
        epoch: _Optional[int] = ...,
    ) -> None: ...

class FetchConsumerGroupAssignmentsResponse(_message.Message):
    __slots__ = ["assignments", "epoch"]
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    assignments: _containers.RepeatedCompositeFieldContainer[
        PartitionAssignment
    ]
    epoch: int
    def __init__(
        self,
        epoch: _Optional[int] = ...,
        assignments: _Optional[
            _Iterable[_Union[PartitionAssignment, _Mapping]]
        ] = ...,
    ) -> None: ...

class FetchCursorRequest(_message.Message):
    __slots__ = ["cursorId", "partition", "stream"]
    CURSORID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    cursorId: str
    partition: int
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partition: _Optional[int] = ...,
        cursorId: _Optional[str] = ...,
    ) -> None: ...

class FetchCursorResponse(_message.Message):
    __slots__ = ["offset"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    offset: int
    def __init__(self, offset: _Optional[int] = ...) -> None: ...

class FetchMetadataRequest(_message.Message):
    __slots__ = ["groups", "streams"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedScalarFieldContainer[str]
    streams: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        streams: _Optional[_Iterable[str]] = ...,
        groups: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class FetchMetadataResponse(_message.Message):
    __slots__ = ["brokers", "groupMetadata", "streamMetadata"]
    BROKERS_FIELD_NUMBER: _ClassVar[int]
    GROUPMETADATA_FIELD_NUMBER: _ClassVar[int]
    STREAMMETADATA_FIELD_NUMBER: _ClassVar[int]
    brokers: _containers.RepeatedCompositeFieldContainer[Broker]
    groupMetadata: _containers.RepeatedCompositeFieldContainer[
        ConsumerGroupMetadata
    ]
    streamMetadata: _containers.RepeatedCompositeFieldContainer[StreamMetadata]
    def __init__(
        self,
        brokers: _Optional[_Iterable[_Union[Broker, _Mapping]]] = ...,
        streamMetadata: _Optional[
            _Iterable[_Union[StreamMetadata, _Mapping]]
        ] = ...,
        groupMetadata: _Optional[
            _Iterable[_Union[ConsumerGroupMetadata, _Mapping]]
        ] = ...,
    ) -> None: ...

class FetchPartitionMetadataRequest(_message.Message):
    __slots__ = ["partition", "stream"]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partition: int
    stream: str
    def __init__(
        self, stream: _Optional[str] = ..., partition: _Optional[int] = ...
    ) -> None: ...

class FetchPartitionMetadataResponse(_message.Message):
    __slots__ = ["metadata"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: PartitionMetadata
    def __init__(
        self, metadata: _Optional[_Union[PartitionMetadata, _Mapping]] = ...
    ) -> None: ...

class JoinConsumerGroupOp(_message.Message):
    __slots__ = ["consumerId", "groupId", "streams"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    groupId: str
    streams: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        consumerId: _Optional[str] = ...,
        streams: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class JoinConsumerGroupRequest(_message.Message):
    __slots__ = ["consumerId", "groupId", "streams"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    groupId: str
    streams: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        consumerId: _Optional[str] = ...,
        streams: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class JoinConsumerGroupResponse(_message.Message):
    __slots__ = [
        "consumerTimeout",
        "coordinator",
        "coordinatorTimeout",
        "epoch",
    ]
    CONSUMERTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    COORDINATORTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    consumerTimeout: int
    coordinator: str
    coordinatorTimeout: int
    epoch: int
    def __init__(
        self,
        coordinator: _Optional[str] = ...,
        epoch: _Optional[int] = ...,
        consumerTimeout: _Optional[int] = ...,
        coordinatorTimeout: _Optional[int] = ...,
    ) -> None: ...

class LeaveConsumerGroupOp(_message.Message):
    __slots__ = ["consumerId", "expired", "groupId"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    expired: bool
    groupId: str
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        consumerId: _Optional[str] = ...,
        expired: bool = ...,
    ) -> None: ...

class LeaveConsumerGroupRequest(_message.Message):
    __slots__ = ["consumerId", "groupId"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    groupId: str
    def __init__(
        self, groupId: _Optional[str] = ..., consumerId: _Optional[str] = ...
    ) -> None: ...

class LeaveConsumerGroupResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class Message(_message.Message):
    __slots__ = [
        "ackInbox",
        "ackPolicy",
        "correlationId",
        "headers",
        "key",
        "offset",
        "partition",
        "replySubject",
        "stream",
        "subject",
        "timestamp",
        "value",
    ]

    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[bytes] = ...
        ) -> None: ...
    ACKINBOX_FIELD_NUMBER: _ClassVar[int]
    ACKPOLICY_FIELD_NUMBER: _ClassVar[int]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    REPLYSUBJECT_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ackInbox: str
    ackPolicy: AckPolicy
    correlationId: str
    headers: _containers.ScalarMap[str, bytes]
    key: bytes
    offset: int
    partition: int
    replySubject: str
    stream: str
    subject: str
    timestamp: int
    value: bytes
    def __init__(
        self,
        offset: _Optional[int] = ...,
        key: _Optional[bytes] = ...,
        value: _Optional[bytes] = ...,
        timestamp: _Optional[int] = ...,
        stream: _Optional[str] = ...,
        partition: _Optional[int] = ...,
        subject: _Optional[str] = ...,
        replySubject: _Optional[str] = ...,
        headers: _Optional[_Mapping[str, bytes]] = ...,
        ackInbox: _Optional[str] = ...,
        correlationId: _Optional[str] = ...,
        ackPolicy: _Optional[_Union[AckPolicy, str]] = ...,
    ) -> None: ...

class NullableBool(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class NullableInt32(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class NullableInt64(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class PartitionAssignment(_message.Message):
    __slots__ = ["partitions", "stream"]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class PartitionEventTimestamps(_message.Message):
    __slots__ = ["firstTimestamp", "latestTimestamp"]
    FIRSTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LATESTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    firstTimestamp: int
    latestTimestamp: int
    def __init__(
        self,
        firstTimestamp: _Optional[int] = ...,
        latestTimestamp: _Optional[int] = ...,
    ) -> None: ...

class PartitionMetadata(_message.Message):
    __slots__ = [
        "highWatermark",
        "id",
        "isr",
        "leader",
        "messagesReceivedTimestamps",
        "newestOffset",
        "pauseTimestamps",
        "paused",
        "readonly",
        "readonlyTimestamps",
        "replicas",
    ]
    HIGHWATERMARK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISR_FIELD_NUMBER: _ClassVar[int]
    LEADER_FIELD_NUMBER: _ClassVar[int]
    MESSAGESRECEIVEDTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    NEWESTOFFSET_FIELD_NUMBER: _ClassVar[int]
    PAUSED_FIELD_NUMBER: _ClassVar[int]
    PAUSETIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    READONLYTIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    highWatermark: int
    id: int
    isr: _containers.RepeatedScalarFieldContainer[str]
    leader: str
    messagesReceivedTimestamps: PartitionEventTimestamps
    newestOffset: int
    pauseTimestamps: PartitionEventTimestamps
    paused: bool
    readonly: bool
    readonlyTimestamps: PartitionEventTimestamps
    replicas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        id: _Optional[int] = ...,
        leader: _Optional[str] = ...,
        replicas: _Optional[_Iterable[str]] = ...,
        isr: _Optional[_Iterable[str]] = ...,
        highWatermark: _Optional[int] = ...,
        newestOffset: _Optional[int] = ...,
        paused: bool = ...,
        readonly: bool = ...,
        messagesReceivedTimestamps: _Optional[
            _Union[PartitionEventTimestamps, _Mapping]
        ] = ...,
        pauseTimestamps: _Optional[
            _Union[PartitionEventTimestamps, _Mapping]
        ] = ...,
        readonlyTimestamps: _Optional[
            _Union[PartitionEventTimestamps, _Mapping]
        ] = ...,
    ) -> None: ...

class PauseStreamOp(_message.Message):
    __slots__ = ["partitions", "resumeAll", "stream"]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    RESUMEALL_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]
    resumeAll: bool
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
        resumeAll: bool = ...,
    ) -> None: ...

class PauseStreamRequest(_message.Message):
    __slots__ = ["name", "partitions", "resumeAll"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    RESUMEALL_FIELD_NUMBER: _ClassVar[int]
    name: str
    partitions: _containers.RepeatedScalarFieldContainer[int]
    resumeAll: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
        resumeAll: bool = ...,
    ) -> None: ...

class PauseStreamResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class PublishAsyncError(_message.Message):
    __slots__ = ["code", "message"]

    class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__: List[str] = []
    BAD_REQUEST: PublishAsyncError.Code
    CODE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FAILED: PublishAsyncError.Code
    INCORRECT_OFFSET: PublishAsyncError.Code
    INTERNAL: PublishAsyncError.Code
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND: PublishAsyncError.Code
    PERMISSION_DENIED: PublishAsyncError.Code
    READONLY: PublishAsyncError.Code
    UNKNOWN: PublishAsyncError.Code
    code: PublishAsyncError.Code
    message: str
    def __init__(
        self,
        code: _Optional[_Union[PublishAsyncError.Code, str]] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...

class PublishRequest(_message.Message):
    __slots__ = [
        "ackInbox",
        "ackPolicy",
        "correlationId",
        "expectedOffset",
        "headers",
        "key",
        "partition",
        "stream",
        "value",
    ]

    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[bytes] = ...
        ) -> None: ...
    ACKINBOX_FIELD_NUMBER: _ClassVar[int]
    ACKPOLICY_FIELD_NUMBER: _ClassVar[int]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    EXPECTEDOFFSET_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ackInbox: str
    ackPolicy: AckPolicy
    correlationId: str
    expectedOffset: int
    headers: _containers.ScalarMap[str, bytes]
    key: bytes
    partition: int
    stream: str
    value: bytes
    def __init__(
        self,
        key: _Optional[bytes] = ...,
        value: _Optional[bytes] = ...,
        stream: _Optional[str] = ...,
        partition: _Optional[int] = ...,
        headers: _Optional[_Mapping[str, bytes]] = ...,
        ackInbox: _Optional[str] = ...,
        correlationId: _Optional[str] = ...,
        ackPolicy: _Optional[_Union[AckPolicy, str]] = ...,
        expectedOffset: _Optional[int] = ...,
    ) -> None: ...

class PublishResponse(_message.Message):
    __slots__ = ["ack", "asyncError", "correlationId"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ASYNCERROR_FIELD_NUMBER: _ClassVar[int]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    ack: Ack
    asyncError: PublishAsyncError
    correlationId: str
    def __init__(
        self,
        ack: _Optional[_Union[Ack, _Mapping]] = ...,
        asyncError: _Optional[_Union[PublishAsyncError, _Mapping]] = ...,
        correlationId: _Optional[str] = ...,
    ) -> None: ...

class PublishToSubjectRequest(_message.Message):
    __slots__ = [
        "ackInbox",
        "ackPolicy",
        "correlationId",
        "headers",
        "key",
        "subject",
        "value",
    ]

    class HeadersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[bytes] = ...
        ) -> None: ...
    ACKINBOX_FIELD_NUMBER: _ClassVar[int]
    ACKPOLICY_FIELD_NUMBER: _ClassVar[int]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ackInbox: str
    ackPolicy: AckPolicy
    correlationId: str
    headers: _containers.ScalarMap[str, bytes]
    key: bytes
    subject: str
    value: bytes
    def __init__(
        self,
        key: _Optional[bytes] = ...,
        value: _Optional[bytes] = ...,
        subject: _Optional[str] = ...,
        headers: _Optional[_Mapping[str, bytes]] = ...,
        ackInbox: _Optional[str] = ...,
        correlationId: _Optional[str] = ...,
        ackPolicy: _Optional[_Union[AckPolicy, str]] = ...,
    ) -> None: ...

class PublishToSubjectResponse(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: Ack
    def __init__(
        self, ack: _Optional[_Union[Ack, _Mapping]] = ...
    ) -> None: ...

class ReportConsumerGroupCoordinatorRequest(_message.Message):
    __slots__ = ["consumerId", "coordinator", "epoch", "groupId"]
    CONSUMERID_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    consumerId: str
    coordinator: str
    epoch: int
    groupId: str
    def __init__(
        self,
        groupId: _Optional[str] = ...,
        consumerId: _Optional[str] = ...,
        coordinator: _Optional[str] = ...,
        epoch: _Optional[int] = ...,
    ) -> None: ...

class ReportConsumerGroupCoordinatorResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class ResumeStreamOp(_message.Message):
    __slots__ = ["partitions", "stream"]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
    ) -> None: ...

class SetCursorRequest(_message.Message):
    __slots__ = ["cursorId", "offset", "partition", "stream"]
    CURSORID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    cursorId: str
    offset: int
    partition: int
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partition: _Optional[int] = ...,
        cursorId: _Optional[str] = ...,
        offset: _Optional[int] = ...,
    ) -> None: ...

class SetCursorResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class SetStreamReadonlyOp(_message.Message):
    __slots__ = ["partitions", "readonly", "stream"]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    partitions: _containers.RepeatedScalarFieldContainer[int]
    readonly: bool
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
        readonly: bool = ...,
    ) -> None: ...

class SetStreamReadonlyRequest(_message.Message):
    __slots__ = ["name", "partitions", "readonly"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    name: str
    partitions: _containers.RepeatedScalarFieldContainer[int]
    readonly: bool
    def __init__(
        self,
        name: _Optional[str] = ...,
        partitions: _Optional[_Iterable[int]] = ...,
        readonly: bool = ...,
    ) -> None: ...

class SetStreamReadonlyResponse(_message.Message):
    __slots__: List[str] = []
    def __init__(self) -> None: ...

class StreamMetadata(_message.Message):
    __slots__ = ["creationTimestamp", "error", "name", "partitions", "subject"]

    class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__: List[str] = []

    class PartitionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: PartitionMetadata
        def __init__(
            self,
            key: _Optional[int] = ...,
            value: _Optional[_Union[PartitionMetadata, _Mapping]] = ...,
        ) -> None: ...
    CREATIONTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OK: StreamMetadata.Error
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STREAM: StreamMetadata.Error
    creationTimestamp: int
    error: StreamMetadata.Error
    name: str
    partitions: _containers.MessageMap[int, PartitionMetadata]
    subject: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        subject: _Optional[str] = ...,
        error: _Optional[_Union[StreamMetadata.Error, str]] = ...,
        partitions: _Optional[_Mapping[int, PartitionMetadata]] = ...,
        creationTimestamp: _Optional[int] = ...,
    ) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = [
        "consumer",
        "partition",
        "readISRReplica",
        "resume",
        "startOffset",
        "startPosition",
        "startTimestamp",
        "stopOffset",
        "stopPosition",
        "stopTimestamp",
        "stream",
    ]
    CONSUMER_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    READISRREPLICA_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    STARTOFFSET_FIELD_NUMBER: _ClassVar[int]
    STARTPOSITION_FIELD_NUMBER: _ClassVar[int]
    STARTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOPOFFSET_FIELD_NUMBER: _ClassVar[int]
    STOPPOSITION_FIELD_NUMBER: _ClassVar[int]
    STOPTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STREAM_FIELD_NUMBER: _ClassVar[int]
    consumer: Consumer
    partition: int
    readISRReplica: bool
    resume: bool
    startOffset: int
    startPosition: StartPosition
    startTimestamp: int
    stopOffset: int
    stopPosition: StopPosition
    stopTimestamp: int
    stream: str
    def __init__(
        self,
        stream: _Optional[str] = ...,
        partition: _Optional[int] = ...,
        startPosition: _Optional[_Union[StartPosition, str]] = ...,
        startOffset: _Optional[int] = ...,
        startTimestamp: _Optional[int] = ...,
        readISRReplica: bool = ...,
        resume: bool = ...,
        stopPosition: _Optional[_Union[StopPosition, str]] = ...,
        stopOffset: _Optional[int] = ...,
        stopTimestamp: _Optional[int] = ...,
        consumer: _Optional[_Union[Consumer, _Mapping]] = ...,
    ) -> None: ...

class StartPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []

class StopPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []

class AckPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []

class ActivityStreamOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__: List[str] = []
