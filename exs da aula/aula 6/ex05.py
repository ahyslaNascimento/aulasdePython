# 5. Encontrar a Posição do Maior Valor em uma Lista:

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

maior = lista[0]

posicao_maior = 0

for i in range(1, len(lista)):

    if lista[i] > maior:

        maior = lista[i]

        posicao_maior = i

print("A posição do maior valor na lista é:", {posicao_maior})

