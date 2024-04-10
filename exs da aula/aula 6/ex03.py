# 3. Encontrar a Média dos Valores em uma Lista:

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

soma = sum(lista)

media = soma / len(lista)

print("A média dos valores na lista é:", {media})