# 1. Encontrar o Maior Valor em uma Lista:

lista = [int(x) for x in input("Digite os valores da lista separados por espaço: ").split()]
maior_valor = lista[0]
i = 1
while i < len(lista):
    if lista[i] > maior_valor:
        maior_valor = lista[i]
    i += 1