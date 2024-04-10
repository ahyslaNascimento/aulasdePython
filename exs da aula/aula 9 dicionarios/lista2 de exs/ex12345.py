'''
1. Crie um dicionário que mapeie nomes de frutas para seus preços. Em 
seguida, utilize os métodos keys(), values() e items() para imprimir as 
chaves, valores e pares chave-valor do dicionário, respectivamente.
'''

frutas = {'pera':5.00, 'uva': 10.00, 'maçã':6.00, 'abacaxi':20.00}
print(frutas.keys()) #usando o keys para pegar somente as chaves do dicionario
print(frutas.values()) #usando values para pegar apenas os valores do dicionario
print(frutas.items()) #usando items para pegar todos os itens do dicionario


'''
2. Crie um dicionário que mapeie nomes de países para suas capitais. 
Utilize o método get() para buscar a capital de um país específico, tratando 
o caso de chave inexistente.
'''

paises = {'França':'Paris', 'Escócia':'Edimburgo', 'Irlanda':'Dublin', 'Grécia':'Atenas'}

pais = 'França'

capital = paises.get(pais,'Capital não encontrada') #usando get para pegar somente a capital do pais frança 

print(f'A capital da {pais} é {capital}.')

'''
3. Crie um dicionário que mapeie nomes de pessoas para suas idades. 
Utilize o método in para verificar se uma pessoa está presente no 
dicionário e, se estiver, imprima sua idade.
'''

nomes = {'Kelen': 34, 'Ahysla': 22, 'Ana': 18, 'Fernanda': 20}

nome = 'Kelen'

if nome in nomes: 
    print(f'A idade de {nome} é {nomes[nome]}')

else:
    print(f'{nome} não encontrada')
    
'''
4. Crie um dicionário vazio e adicione pares chave-valor utilizando o 
método update(). O dicionário deve mapear nomes de animais para seus 
sons
'''

animais = {}

animais.update({'cachorro': 'au au', 'gato':'miau', 'passarinho':'piu piu', 'galo': 'cocoricó'}) #usando update para adicionar itens ao dicionario vazio
print(animais)

'''Crie um dicionário que mapeie números de telefone para nomes de 
pessoas. Utilize o método pop() para remover um número de telefone do 
dicionário e, em seguida, verifique se a chave foi removida
'''
telefones = {51984098905:'Carla', 51988503640:'Joel', 51994269967:'Pedro'}

telefones.pop(51994269967) #usando pop para remover uma chave e seu valor do dicionario
print(telefones)