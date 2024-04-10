tupleImpares = ()

for i in range (1, 11): #percorrendo os numeros de 1 a 10
    if i % 2 == 1: #verificando se o numero é impar
        tupleImpares += (i,) #adicionando numero impar a tupla com o operador de concatenação
        print(tupleImpares)