def par_ou_impar(numero):
    return numero % 2 == 0 #retornando o resto da divisao para verificar se o número é par


num = int(input("Digite um número: "))

if par_ou_impar(num): #condição para mostrar na tela que o número é par
    print("É um número par.")
else:   #se a primeira condição for falsa aparecerá na tela que o número é ímpar 
    print("É um número ímpar.")