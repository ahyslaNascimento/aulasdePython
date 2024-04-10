'''
Percorra um dicionário que armazena informações de contato (nome, 
telefone, email) e imprima cada item em um formato amigável. 
Calcule a soma dos valores de um dicionário que armazene os preços de 
diferentes produtos. 
Crie um novo dicionário contendo apenas as chaves com valores maiores 
que um determinado valor em um dicionário original.
'''

informacoesDecontato = {
    'nome': 'Ahysla',
    'telefone': '51984098906',
    'email': 'ahys@gmail.com'
}


print("Informações de contato:")
for chave, valor in informacoesDecontato.items():
    print(f"{chave.capitalize()}: {valor}")







precosProdutos = {'produto1': 10, 'produto2': 20, 'produto3': 30}


somaPrecos = sum(precosProdutos.values())
print("Soma dos preços dos produtos:", somaPrecos)







dicionario_original = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


valor_limite = 2
novo_dicionario = {chave: valor for chave, valor in dicionario_original.items() if valor > valor_limite}
print("Novo dicionário com chaves maiores que", valor_limite, ":", novo_dicionario)
