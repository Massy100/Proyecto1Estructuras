from Double_Linked_List import DoublyLinkedList
from simple_linked_list import SimplyLinkedList

lista1 = DoublyLinkedList()

lista1.append(1)
lista1.append(2)
lista1.append(3)

print(lista1.transversal())

# ----------------------------
lista2 = SimplyLinkedList()
lista2.append(1)
lista2.append(2)
lista2.append(3)

print(lista2.transversal())
