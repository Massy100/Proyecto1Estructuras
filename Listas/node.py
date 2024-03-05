from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, data: T):
        self.__data: T = data
        self.__next: Optional['Node[T]'] = None
    
    # Getter para 'data'
    @property
    def data(self) -> T:
        return self.__data

    # Setter para 'data'
    @data.setter
    def data(self, value: T) -> None:
        self.__data = value

    # Getter para 'next'
    @property
    def next(self) -> Optional['Node[T]']:
        return self.__next

    # Setter para 'next'
    @next.setter
    def next(self, value: Optional['Node[T]']) -> None:
        self.__next = value
