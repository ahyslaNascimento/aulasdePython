import random

numeroSecreto = random.randint(1,100)
tentativas = 0

while True:
    
    palpite = int(input("Dê seu palpite digitando um numero entre 1 e 100: "))
    
    tentativas += 1
    if palpite == numeroSecreto:
        print(f"Parabéns você acertou o numero em", tentativas, "tentativas.")
    elif palpite < numeroSecreto:
        print(f"tente um numero maior")
    else: palpite != numeroSecreto
    print(f"tente um numero menor")