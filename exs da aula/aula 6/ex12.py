lista = [int(x) for x in input("Digite sua lista: ").split()]
metade = len(lista) // 2

lista1 = lista[:metade]
lista2 = lista[metade:]

print(f"Listas dividas", lista1, lista2)