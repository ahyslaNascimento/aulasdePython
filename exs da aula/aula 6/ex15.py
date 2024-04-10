lista = [int(x) for x in input("Digite uma lista: ").split()]
numero = int(input("Digite o numero que deseja adicionar a lista: "))

lista.append(numero)
print(f"Numero adicionado a lista", numero)
print(f"Lista atualizada", lista)
