from Listas.simple_linked_list import SimplyLinkedList

numeros = SimplyLinkedList[int]

numeros.append(2)
numeros.append(4)
numeros.append(6)
numeros.prepend(1)
numeros.prepend(5)
numeros.prepend(3)

numeros.transversal()
numeros.reverse_transversal()