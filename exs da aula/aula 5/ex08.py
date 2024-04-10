tuplePares = ()

for i in range (1, 11): #percorrendo os numeros de 1 a 10
    if i % 2 == 0: #verificando se o numero é par
        tuplePares += (i,) #adicionando o numero par a tupla utilizando o operador de concatenação
        print(tuplePares)

