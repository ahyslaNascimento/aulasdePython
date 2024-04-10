def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

num = int(input("Digite um número: "))

print(f"O fatorial de {num} é: {fatorial(num)}")
