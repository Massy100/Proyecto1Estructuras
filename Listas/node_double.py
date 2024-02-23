from typing import TypeVar, Generic
T = TypeVar("T")

class NodeDouble(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: NodeDouble | None = None
        self.prev: NodeDouble | None = None
