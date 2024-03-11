from Listas.node import Node
from typing import TypeVar, Generic

T = TypeVar("T")


class CircularList(Generic[T]):
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__size: int = 0

    def append(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__tail.next = self.__head

        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__tail.next = self.__head
        self.__size += 1

    def is_empty(self):
        return self.__head is None and self.__tail is None

    def prepend(self, data: T):
        new_node = Node(data)
        # la lista esta vacia (mover dos punteros, head y tail)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            new_node.next = self.__head
            self.__size += 1
        # la lista tiene al menos un elemento (mover solo head)
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__tail.next = self.__head
            self.__size += 1

        # Recorrer la lista

    def transversal(self) -> str:
        current = self.__head
        result = ''
        while current is not self.__tail:
            result += str(current.data) + "\n"
            current = current.next

        if current is not None:
            result += str(current.data) + "\n"

        return result
    
    def show(self):
        """
        Muestra los elementos de la lista enlazada.
        """
        return self.transversal()

    def find_by(self, data: T) -> Node:
        current = self.__head

        while current is not None:
            if current.data == data:
                return current

            else:
                current = current.next

            if current == self.__head:
                break
        raise Exception("El elemento no existe")

    # ELIMINAR AL INICIO

    def pop(self):
        if self.is_empty():
            raise Exception('No hay elementos por eliminar')

        elif self.__head is self.__tail:
            current = self.__head
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return current
        else:
            current = self.__head
            self.__head = current.next
            self.__tail.next = None
            current.next = None
            self.__tail.next = self.__head
            self.__size -= 1
            return current

    def remove_by_id(self, value):
        if self.is_empty():
            raise Exception("La lista está vacía")

        current = self.__head
        if current.data.codigo_usuario == value:
            self.__head = current.next
            self.__size -= 1
            return current.data

        prev = None
        while current is not None:
            if current.data.codigo_usuario == value:
                prev.next = current.next
                self.__size -= 1
                return current.data
            prev = current
            current = current.next

