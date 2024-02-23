from node import Node
from typing import TypeVar, Generic

T = TypeVar("T")
class CircularList(Generic[T]):
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0


    def append(self,data: T):
        new_node= Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def is_empty(self):
        return self.head is None and self.tail is None

    def prepend(self, data: T):
        new_node = Node(data)
        # la lista esta vacia (mover dos punteros, head y tail)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            self.size += 1
        # la lista tiene al menos un elemento (mover solo head)
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.size += 1

        # Recorrer la lista
    def transversal(self) -> str:
        current = self.head
        result = ''
        while current is not self.tail:
            result += str(current.data) + '->'
            current = current.next

        if current is not None:
            result += str(current.data)

        return result


    def find_by(self, data: T) -> Node:
        current = self.head

        while current is not None:
            if current.data ==  data:
                return current

            else:
                current = current.next

            if current == self.head:
                break
        raise Exception("El elemento no existe")

    #ELIMINAR AL INICIO


    def pop(self):
        if self.is_empty():
            raise Exception('No hay elementos por eliminar')

        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current
        else:
            current = self.head
            self.head = current.next
            self.tail.next = None
            current.next = None
            self.tail.next = self.head
            self.size -= 1
            return current

