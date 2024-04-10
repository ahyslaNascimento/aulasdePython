tuple = ('banana', 'abacate', 'kiwi')
x = list(tuple) #transformando tupla em lista para remover elemento
x.remove('abacate') #removendo abacate da lista usando .remove
tuple = (x)

print(tuple)