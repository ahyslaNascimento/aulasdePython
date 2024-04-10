tuple = (5, 2, 8, 1, 3)
tupleOrdenadacrescente = tuple(sorted(tuple)) #ordenando os elementos em ordem crescente usando sorted  
print("Tupla ordenada (crescente):", tupleOrdenadacrescente)

tupleOrdenadadecrescente = tuple(sorted(tuple, reverse=True)) #ordenando em ordem descrescente usando reverse
print("Tupla ordenada (decrescente):", tupleOrdenadadecrescente)
