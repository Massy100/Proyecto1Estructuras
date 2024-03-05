from typing import TypeVar, Generic
from Listas.node_double import NodeDouble

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.__head: NodeDouble | None = None
        self.__tail: NodeDouble | None = None
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__head is None and self.__tail is None

    def insert_empty(self, data: T):
        new_node = NodeDouble(data)
        self.__head = new_node
        self.__tail = new_node
        self.__size = 1
        
    # METODOS DE INSERCION
    # inserta por la cabeza (orden descendente)
    def prepend(self, data: T):
        if self.is_empty():
            self.insert_empty(data)
        else:
            new_node = NodeDouble(data)
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
            self.__size += 1
    
    # inserta por la cola (orden ascendente)
    def append(self, data: T):
        if self.is_empty():
            self.insert_empty(data)

        else:
            new_node = NodeDouble(data)
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
            self.__size += 1
            
    def insert_at_post(self, pos: int, data: T):
        if pos == 0:
            self.prepend(data)

        elif pos == self.__size - 1:
            self.append(data)

        else:
            ref = self.find_at(pos)
            next_node = ref.next
            new_node = NodeDouble(data)
            new_node.next = next_node
            new_node.prev = ref
            ref.next = new_node
            next_node.prev = new_node
            self.__size += 1

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
            self.__size += 1
            
            
    # METODOS DE ELIMINACION
    # elimina por la cabeza
    def unshift(self):
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")

        elif self.__head is self.__tail:
            ref = self.__head
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.__head
            self.__head = ref.next
            ref.next = None
            self.__head.prev = None
            self.size -= 1
            return ref
        
    # elimina por la cola
    def pop(self) -> NodeDouble:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.__head is self.__tail:
            ref = self.__tail
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.__tail
            self.__tail = self.__tail.prev
            self.__tail.next = None
            ref.prev = None
            self.__size -= 1
            return ref

    def delete_at(self, pos: int) -> NodeDouble:
        if self.is_empty():
            raise Exception("LA LISTA ESTA VACIA")
        elif self.__head is self.__tail:
            ref = self.__tail
            self.__head = None
            self.__tail = None
            self.__size = 0
            return ref
        else:
            ref = self.find_at(pos)
            prev_node = ref.prev
            next_node = ref.next
            prev_node.next = next_node
            next_node.previous = prev_node
            ref.next = None
            ref.prev = None
            self.__size -= 1

            return ref
    
    # METODOS DE BUSQUEDA
    def find_at(self, pos: int) -> NodeDouble:
        current_pos = 0
        ref = self.__head
        while ref is not None:
            if current_pos == pos:
                return ref
            else:
                ref = ref.next
                current_pos += 1

        raise Exception("NO EXISTE LA POSICION")
    
    # METODOS PARA RECORRER
    def transversal(self) -> str:
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data)
            if current is not self.__tail:
                result += "->"
            current = current.next
        return result

    def reverse_transversal(self) -> str:
        result = ""
        current = self.__tail
        while current is not None:
            result += str(current.data)
            if current is not self.__head:
                result += "->"
            current = current.prev
        return result

    
