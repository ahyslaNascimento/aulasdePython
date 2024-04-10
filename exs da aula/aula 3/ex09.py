saldo = 0
while True:
    print("1. Saldo")
    print("2. Saque")
    print("3. Depósito")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Seu saldo é:", saldo)
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        if valor <= saldo:
            saldo -= valor
            print("Saque de", valor, "realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    elif opcao == 3:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print("Depósito de", valor, "realizado com sucesso.")
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

