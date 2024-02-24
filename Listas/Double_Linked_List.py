from typing import TypeVar, Generic
from Listas.node_double import NodeDouble

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: NodeDouble | None = None
        self.tail: NodeDouble | None = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def insert_empty(self, data: T):
        new_node = NodeDouble(data)
        self.head = new_node
        self.tail = new_node
        self.size = 1

    def prepend(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = NodeDouble(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1

    def append(self, data: T):
        if self.is_empty():
            self.insert_empty(data)

        else:
            new_node = NodeDouble(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1

    def transversal(self) -> str:
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data)
            if current is not self.tail:
                result += "->"
            current = current.next
        return result

    def reverse_transversal(self) -> str:
        result = ""
        current = self.tail
        while current is not None:
            result += str(current.data)
            if current is not self.head:
                result += "->"
            current = current.prev
        return result

    def find_at(self, pos: int) -> NodeDouble:
        current_pos = 0
        ref = self.head
        while ref is not None:
            if current_pos == pos:
                return ref
            else:
                ref = ref.next
                current_pos += 1

        raise Exception("NO EXISTE LA POSICION")

    def insert_at_post(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)

        elif pos == self.size - 1:
            self.append(data)

        else:
            ref = self.find_at(pos)
            next_node = ref.next
            new_node = NodeDouble(data)
            new_node.next = next_node
            new_node.prev = ref
            ref.next = new_node
            next_node.prev = new_node
            self.size += 1

    def insert_at_prev(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            new_node = NodeDouble(data)
            new_node.prev = prev_node
            new_node.next = ref
            ref.prev = new_node
            prev_node.next = new_node
            self.size += 1

    def unshift(self):
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")

        elif self.head is self.tail:
            ref = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.head
            self.head = ref.next
            ref.next = None
            self.head.prev = None
            self.size -= 1
            return ref

    def pop(self) -> NodeDouble:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.head is self.tail:
            ref = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            ref.prev = None
            self.size -= 1
            return ref

    def delete_at(self, pos: int) -> NodeDouble:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.head is self.tail:
            ref = self.tail
            self.head = None
            self.tail = None
            self.size = 0
            return ref
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            next_node = ref.next
            prev_node.next = next_node
            next_node.previous = prev_node
            ref.next = None
            ref.prev = None
            self.size -= 1

            return ref
