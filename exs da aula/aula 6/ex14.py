lista = [int(x) for x in input("Digite uma lista: ").split()]
numero = int(input("Digite o numero que deseja remover da lista: "))

if numero in lista:
    lista.remove(numero)
    print(f"Numero removido", numero)
    print(f"Lista atualizada", lista)
else:
    print(f"Este numero não está na lista.")