from dataclasses import dataclass
from functools import cached_property
from typing import Any
from typing import Generic
from typing import TypedDict
from typing import TypeVar
from typing import cast

from dipdup.fetcher import HasLevel
from dipdup.runtimes import SubstrateRuntime


class BlockHeader(TypedDict):
    hash: str
    number: int
    daHeight: str
    transactionsRoot: str
    transactionsCount: int
    messageReceiptCount: int
    prevRoot: str
    time: str
    applicationHash: str
    eventInboxRoot: str
    consensusParametersVersion: int
    stateTransitionBytecodeVersion: int
    messageOutboxRoot: str
    # NOTE: There are more fields in header
    specVersion: str


@dataclass(frozen=True)
class SubstrateEventData(HasLevel):
    name: str
    index: int
    extrinsicIndex: int
    callAddress: list[str]
    args: list[Any]
    header: BlockHeader

    @property
    def level(self) -> int:  # type: ignore[override]
        return self.header['number']


PayloadT = TypeVar('PayloadT')


@dataclass(frozen=True)
class SubstrateEvent(Generic[PayloadT]):
    data: SubstrateEventData
    runtime: SubstrateRuntime

    @cached_property
    def payload(self) -> PayloadT:
        return cast(
            PayloadT,
            self.runtime.decode_event_args(
                name=self.name,
                args=self.data.args,
                spec_version=self.data.header['specVersion'],
            ),
        )

    @property
    def level(self) -> int:
        return self.data.level

    @property
    def name(self) -> str:
        return self.data.name
