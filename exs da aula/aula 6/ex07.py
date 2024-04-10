# 7. Verificar se um Valor Está Presente em uma Lista:

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

valor = int(input("Digite o valor que deseja verificar: "))

if valor in lista:

    print("O valor", {valor}, "está presente na lista.")

else:

    print("O valor", {valor}, "não está presente na lista.")

