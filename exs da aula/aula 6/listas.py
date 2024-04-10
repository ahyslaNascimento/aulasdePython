# 1. Encontrar o Maior Valor em uma Lista
lista = [int(x) for x in input("Digite os valores da lista separados por espaço: ").split()]
maior_valor = lista[0]
i = 1
while i < len(lista):
    if lista[i] > maior_valor:
        maior_valor = lista[i]
    i += 1
print("O maior valor na lista é:", maior_valor)

# 2. Encontrar a Soma dos Valores em uma Lista
soma = 0
i = 0
while i < len(lista):
    soma += lista[i]
    i += 1
print("A soma dos valores na lista é:", soma)

# 3. Encontrar a Média dos Valores em uma Lista
media = soma / len(lista)
print("A média dos valores na lista é:", media)

# 4. Encontrar a Posição do Menor Valor em uma Lista
menor_valor = lista[0]
posicao_menor = 0
i = 1
while i < len(lista):
    if lista[i] < menor_valor:
        menor_valor = lista[i]
        posicao_menor = i
    i += 1
print("A posição do menor valor na lista é:", posicao_menor)

# 5. Encontrar a Posição do Maior Valor em uma Lista
posicao_maior = 0
i = 1
while i < len(lista):
    if lista[i] > lista[posicao_maior]:
        posicao_maior = i
    i += 1
print("A posição do maior valor na lista é:", posicao_maior)

# 6. Encontrar o Número de Vezes que um Valor Aparece em uma Lista
valor = int(input("Digite o valor que deseja verificar na lista: "))
contador = 0
i = 0
while i < len(lista):
    if lista[i] == valor:
        contador += 1
    i += 1
print("O valor", valor, "aparece", contador, "vezes na lista.")

# 7. Verificar se um Valor Está Presente em uma Lista
valor = int(input("Digite o valor que deseja verificar na lista: "))
encontrado = False
i = 0
while i < len(lista):
    if lista[i] == valor:
        encontrado = True
        break
    i += 1
if encontrado:
    print("O valor", valor, "está presente na lista.")
else:
    print("O valor", valor, "não está presente na lista.")

# 8. Gerar uma Lista com Valores Pares de 1 a 10
lista_pares = []
i = 2
while i <= 10:
    lista_pares.append(i)
    i += 2
print("Lista de valores pares de 1 a 10:", lista_pares)

# 9. Gerar uma Lista com Valores Ímpares de 1 a 10
lista_impares = []
i = 1
while i <= 10:
    lista_impares.append(i)
    i += 2
print("Lista de valores ímpares de 1 a 10:", lista_impares)

# 10. Inverter a Ordem dos Elementos de uma Lista
lista_invertida = []
i = len(lista) - 1
while i >= 0:
    lista_invertida.append(lista[i])
    i -= 1
print("Lista invertida:", lista_invertida)

# 11. Concatenar Duas Listas
outra_lista = [int(x) for x in input("Digite os valores da segunda lista separados por espaço: ").split()]
lista_concatenada = lista + outra_lista
print("Lista concatenada:", lista_concatenada)

# 12. Dividir uma Lista em Duas
metade = len(lista) // 2
primeira_metade = lista[:metade]
segunda_metade = lista[metade:]
print("Primeira metade da lista:", primeira_metade)
print("Segunda metade da lista:", segunda_metade)

# 13. Ordenar os Elementos de uma Lista
i = 0
while i < len(lista):
    j = 0
    while j < len(lista) - 1:
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
        j += 1
    i += 1
print("Lista ordenada:", lista)

# 14. Remover um Elemento de uma Lista
elemento_remover = int(input("Digite o elemento que deseja remover da lista: "))
encontrado = False
i = 0
while i < len(lista):
    if lista[i] == elemento_remover:
        del lista[i]
        encontrado = True
        break
    i += 1
if encontrado:
    print("Elemento removido com sucesso.")
else:
    print("O elemento não está presente na lista.")

# 15. Adicionar um Elemento a uma Lista
elemento_adicionar = int(input("Digite o elemento que deseja adicionar à lista: "))
lista.append(elemento_adicionar)
print("Elemento adicionado com sucesso.")