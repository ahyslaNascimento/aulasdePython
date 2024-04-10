'''
4. Desafio: 
Crie um programa simples de "Adivinhação de palavras" usando um 
dicionário. O dicionário pode armazenar palavras como chaves e suas 
definições como valores. O programa deve selecionar uma palavra aleatória 
do dicionário, mostrar sua definição e pedir ao usuário para adivinhar a 
palavra correta. 
'''


jogoDeAdivinhar = {
    "pera": "fruta verde e em formato de funil",
    "banana": "fruta amarela e alongada",
    "computador": "usa-se diariamente na programação",
    "calculadora": "será sua amiga na hora dos cálculos matemáticos"
    
}


palavras = list(jogoDeAdivinhar.keys())


indice_aleatorio = 0  
if len(palavras) > 1:
   
    indice_aleatorio = hash("random_seed") % len(palavras)


palavra = palavras[indice_aleatorio]
definicao = jogoDeAdivinhar[palavra]


print("Definição:", definicao)


tentativa = input("Adivinhe a palavra: ").lower()


if tentativa == palavra:
    print("Parabéns! Você acertou a palavra.")
else:
    print("Ops! Tente novamente.")