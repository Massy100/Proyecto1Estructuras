from Listas.node import Node
from typing import TypeVar, Generic

T = TypeVar("T")


class SimplyLinkedList(Generic[T]):
    def __init__(self, ):
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def unshift(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def append(self, data: T):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def insert_at(self, data: T, index):
        if index == 0:
            self.unshift(data)
        elif self.is_empty():
            self.unshift(data)
        elif index == self.size:
            self.append(data)
        else:
            new_node = Node(data)
            previous = self.find_at(index - 1)
            new_node.next = previous.next
            previous.next = new_node

            return new_node

    def find_by(self, data: T):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next

        raise Exception("El elemento no esta en la cola")

    def find_at(self, index):
        current = self.head
        contador = 0

        while current is not None:
            if contador == index:
                return current
            else:
                current = current.next
                contador += 1

        raise Exception("La posicion no existe")

    def transversal(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current is not self.tail:
                result += "->"

            current = current.next

        return result

    def reverse_transversal(self):
        pass
