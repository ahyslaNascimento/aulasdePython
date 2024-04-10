#  usuário inserindo o limite da lista
listaLimite = int(input("Insira o limite superior da lista: "))


listaImpares = [] 

contador = 1


while contador <= listaLimite:
    # verifica se o número atual é ímpar
    if contador % 2 == 1:
       
        listaImpares.append(contador)
   
    contador += 1


print("Valores pares de 1 a", listaLimite, ":", listaImpares)

