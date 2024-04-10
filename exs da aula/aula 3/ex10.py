
print("Bem-vindo ao Controle de Estoque!")


produto1 = None
quantidade1 = 0
produto2 = None
quantidade2 = 0

while True:
    print("1. Adicionar produto")
    print("2. Consultar estoque")
    print("3. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        if produto1 is None:
            produto1 = input("Digite o nome do produto: ")
            quantidade1 = int(input("Digite a quantidade: "))
            print("Produto adicionado com sucesso.")
        elif produto2 is None:
            produto2 = input("Digite o nome do produto: ")
            quantidade2 = int(input("Digite a quantidade: "))
            print("Produto adicionado com sucesso.")
        else:
            print("Limite máximo de produtos atingido.")
    
    elif opcao == 2:
        print("Estoque:")
        if produto1 is not None:
            print(f"{produto1}: {quantidade1} unidades")
        if produto2 is not None:
            print(f"{produto2}: {quantidade2} unidades")
    
    elif opcao == 3:
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")


