''' 
3. Adicionando e Removendo Elementos:
• Crie um dicionário vazio e adicione as chaves "nome" e "idade" com seus 
respectivos valores.
• Crie um dicionário com as informações de um produto e remova a chave 
"cor".
• Crie um dicionário com as informações de um livro e adicione a chave 
"tradução" com o valor "Sim".
• Crie um dicionário com as informações de um filme e remova a chave "ano 
de lançamento".

'''

dicionario = dict()
 
dicionario.update({'nome': 'pedro', 'idade':18})

print(dicionario)

meu_dicionario2 = {'produto':'celular', 'preço':2000, 'cor':'azul', 'tamanho': '15cm'}

meu_dicionario2.pop('cor')

print(meu_dicionario2)

meu_dicionario3 = {'título':'A cabana', 'autor':'William P. Young', 'ano de lancamento':2007, 'gênero':' Romance, Suspense, Ficção religiosa'}

meu_dicionario3.update({'tradução':'sim'})

print(meu_dicionario3)

meu_dicionario4 = {'nome':'pulp fiction', 'diretor':'Quentin Tarantino', 'ano de lancamento':1995, 'gênero':'drama policial'}

meu_dicionario4.pop('ano de lancamento')

print(meu_dicionario4)