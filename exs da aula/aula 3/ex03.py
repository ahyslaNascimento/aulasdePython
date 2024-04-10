tabuada = int(input("Digite o numero que deseja ver a tabuada: "))

for numero in range(11):
    resultado = tabuada * numero
    print(f" {tabuada} x {numero} = {resultado}")