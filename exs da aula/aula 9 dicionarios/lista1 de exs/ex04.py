'''
Crie um dicionário com as informações de um amigo e imprima cada chave 
e valor em linhas separadas.
'''

amigo = {'nome':'feliphe', 'idade':18, 'altura': 180}

for chave, valor in amigo.items():
    print(chave, valor)
    
''' 
Crie um dicionário com as informações de um produto e imprima todos os 
valores em uma única linha.
'''
    
meu_dicionario2 = {'produto':'celular', 'preço':2000, 'cor':'azul', 'tamanho': '15cm'}
print(meu_dicionario2.values())


'''
Crie um dicionário com as informações de um livro e imprima as chaves 
"título" e "autor" em uma única linha. 
Crie um dicionário com as informações de um filme e imprima as chaves 
"nome" e "diretor" em uma única linha. 

'''
 

meu_dicionario3 = {'título':'A cabana', 'autor':'William P. Young', 'ano de lancamento':2007, 'gênero':' Romance, Suspense, Ficção religiosa'}
print(list(meu_dicionario3.values())[:2])
meu_dicionario4 = {'nome':'pulp fiction', 'diretor':'Quentin Tarantino', 'ano de lancamento':1995, 'gênero':'drama policial'}
print(list(meu_dicionario4.values())[:2])