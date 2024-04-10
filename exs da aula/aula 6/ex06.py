# 6. Encontrar o Número de Vezes que um Valor Aparece em uma Lista:

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

valor = int(input("Digite o valor que deseja contar: "))

contagem = lista.count(valor)

print("O valor", {valor}, "aparece", {contagem}, "vezes na lista.")