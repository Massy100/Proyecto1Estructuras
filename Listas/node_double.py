from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class NodeDouble(Generic[T]):
    def __init__(self, data: T):
        self.__data: T = data
        self.__next: NodeDouble | None = None
        self.__prev: NodeDouble | None = None
        
        
    @property
    def data(self) -> T:
        """Getter para el atributo __data."""
        return self.__data

    @data.setter
    def data(self, value: T):
        """Setter para el atributo __data."""
        self.__data = value

    @property
    def next(self) -> Optional['NodeDouble[T]']:
        """Getter para el atributo __next."""
        return self.__next

    @next.setter
    def next(self, value: Optional['NodeDouble[T]']):
        """Setter para el atributo __next."""
        self.__next = value

    @property
    def prev(self) -> Optional['NodeDouble[T]']:
        """Getter para el atributo __prev."""
        return self.__prev

    @prev.setter
    def prev(self, value: Optional['NodeDouble[T]']):
        """Setter para el atributo __prev."""
        self.__prev = value
