# 4. Encontrar a Posição do Menor Valor em uma Lista:

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

menor = lista[0]

posicao_menor = 0

for i in range(1, len(lista)):

    if lista[i] < menor:

        menor = lista[i]

        posicao_menor = i

print("A posição do menor valor na lista é:", {posicao_menor})