lista = ['a', 'b', 'c', 'd']
print(lista)
lista.append('e') #  na koncu
print(lista)
lista.insert(1, 'aa')
print(lista)
lista.remove('c')
print(lista)
lista.reverse() # na odwrot
print(lista)
print(lista.pop(3)) # pobiera a nastepnie usuwa
print(lista)
print(lista.index('a')) # pokaze na ktorym miejscu jest
print(lista.count('a')) # przelicza ile razy

lista2 = ['g','h']
lista.extend(lista2)
print(lista)

listakopia = lista.copy()
print(listakopia)
listakopia.clear()
print(listakopia)
