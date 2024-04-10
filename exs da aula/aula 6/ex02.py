lista = [int(x) for x in input("Digite uma lista de números a serem somados: ").split()]
soma = 0 

for num in lista:
    soma += num
    print(f"A soma dos numeros na lista é: ", {soma})
