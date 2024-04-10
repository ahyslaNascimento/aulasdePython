
def soma(a, b):
    return a + b        #retorno da função que soma os numeros

def subtracao(a, b):  
    return a - b    #retorno da função que subtrai os números

def multiplicacao(a, b):        
   return a * b     #usando return para retornar a função que está multiplicando os números
 
def divisao(a, b):
    if b != 0:   #se b for diferente de 0 a divisão será retornada para o usuário
        return a / b #divisão sendo retornada se a condição for atendida
    else:
        return "Erro: Divisão por zero!" #condição para dar erro caso b seja 0 


num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: "))

print(f"Soma: {soma(num1, num2)}")
print(f"Subtração: {subtracao(num1, num2)}")
print(f"Multiplicação: {multiplicacao(num1, num2)}")
print(f"Divisão: {divisao(num1, num2)}")