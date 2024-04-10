'''
Verifique se uma determinada palavra existe como chave em um dicionário 
que simula um dicionário de sinônimos. 
Conte o número de ocorrências de cada letra em uma string usando um 
dicionário. 
Remova do dicionário todas as chaves que possuem valores vazios.
'''

sinonimos = {'feliz': 'alegre', 'triste': 'melancólico', 'raiva': 'ódio'}


palavra = 'melancólico'
if palavra in sinonimos:
    print(f"A palavra '{palavra}' existe no dicionário de sinônimos.")



texto = "piano"
contagem_letras = {}
for letra in texto:
    contagem_letras[letra] = contagem_letras.get(letra, 0) + 1
print("Contagem de ocorrências de cada letra:", contagem_letras)



dicionario = {'a': 1, 'b': '', 'c': 3, 'd': None}
dicionario = {chave: valor for chave, valor in dicionario.items() if valor is not None and valor != ''}
print("Dicionário após remoção das chaves com valores vazios:", dicionario)