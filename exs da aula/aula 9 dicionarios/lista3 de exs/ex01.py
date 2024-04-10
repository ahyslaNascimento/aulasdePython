'''
Crie um dicionário para armazenar informações sobre um filme, incluindo 
título, ano, diretor e atores principais. 
Acesse o ano de lançamento do filme usando a chave apropriada. 
Modifique o valor do diretor para um novo diretor. 
Adicione uma nova chave-valor ao dicionário para incluir a duração do 
filme
'''
filme = {
    'título': 'Pulp Fiction',
    'ano': 1994,
    'diretor': 'Quentin Tarantino',
    'atores_principais': ['John Travolta', 'Uma Thurman', 'Samuel L. Jackson']
}


ano_lancamento = filme['ano']
print("Ano de lançamento do filme:", ano_lancamento)


filme['diretor'] = 'Christopher Nolan'
print("Novo diretor do filme:", filme['diretor'])


filme['duração'] = '154 minutos'
print("Duração do filme:", filme['duração'])
