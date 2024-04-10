#  usuário inserindo o limite da lista
listaLimite = int(input("Insira o limite superior da lista: "))


listaPares = []


contador = 1


while contador <= listaLimite:
    # verifica se o número atual é par
    if contador % 2 == 0:
       
        listaPares.append(contador)
   
    contador += 1


print("Valores pares de 1 a", listaLimite, ":", listaPares)
