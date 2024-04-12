def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero!"

def maior_numero(a, b):
    return max(a, b)

def media_de_tres(a, b, c):
    return (a + b + c) / 3

def par_ou_impar(num):
     num % 2 == 0  
     return "é par"


def tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    elif num == 0:
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado

def area_triangulo(base, altura):
    return 0.5 * base * altura