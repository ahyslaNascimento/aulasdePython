numero = int (input("Digite um numero: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
    
    print(f"O fatoral de {numero} é: {fatorial}")