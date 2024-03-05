from Listas.node import Node
from typing import TypeVar, Generic

T = TypeVar("T")


class SimplyLinkedList(Generic[T]):
    def __init__(self, ):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None and self.__tail is None

    def unshift(self, data: T):
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.__size += 1

    def remove_by_value(self, value):
        if self.is_empty():
            raise Exception("La lista está vacía")

        current = self.__head
        if current.data.nombre == value:
            self.__head = current.next
            self.__size -= 1
            return current.data

        prev = None
        while current is not None:
            if current.data.nombre == value:
                prev.next = current.next
                self.__size -= 1
                return current.data
            prev = current
            current = current.next

        raise ValueError(f"No se encontró ningún nodo con el valor '{value}' en la lista")
    
    def remove_by_id(self, value):
        if self.is_empty():
            raise Exception("La lista está vacía")

        current = self.__head
        if current.data.codigo == value:
            self.__head = current.next
            self.__size -= 1
            return current.data

        prev = None
        while current is not None:
            if current.data.codigo == value:
                prev.next = current.next
                self.__size -= 1
                return current.data
            prev = current
            current = current.next

        raise ValueError(f"No se encontró ningún nodo con el valor '{value}' en la lista")

    def append(self, data: T):
        if self.is_empty():
            new_node = Node(data)
            self.__head = new_node
            self.__tail = new_node
            self.__size += 1
        else:
            new_node = Node(data)
            self.__tail.next = new_node
            self.__tail = new_node
            self.__size += 1

    def insert_at(self, data: T, index):
        if index == 0:
            self.unshift(data)
        elif self.is_empty():
            self.unshift(data)
        elif index == self.__size:
            self.append(data)
        else:
            new_node = Node(data)
            previous = self.find_at(index - 1)
            new_node.next = previous.next
            previous.next = new_node

            return new_node

    def find_by(self, data: T):
        current = self.__head
        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next

        raise Exception("El elemento no esta en la cola")

    def find_at(self, index):
        current = self.__head
        contador = 0

        while current is not None:
            if contador == index:
                return current
            else:
                current = current.next
                contador += 1

        raise Exception("La posicion no existe")

    def transversal(self):
        current = self.__head
        result = ""
        while current is not None:
            result += str(current.data)
            if current is not self.__tail:
                result += "\n"

            current = current.next

        return result

    def show(self):
        """
        Muestra los elementos de la lista enlazada.
        """
        return self.transversal()
