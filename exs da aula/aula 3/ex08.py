
   
palavra_secreta = "python"


letras_adivinhadas = ""


max_tentativas = 6
tentativas = 0


palavra_mostrada = "_" * len(palavra_secreta)

print("Bem-vindo ao Jogo da Forca!")


while tentativas < max_tentativas and "_" in palavra_mostrada:
    print("Palavra:", palavra_mostrada)
    print("Tentativas restantes:", max_tentativas - tentativas)
    
   
    letra = input("Adivinhe uma letra: ").lower()
    
    
    while letra in letras_adivinhadas:
        print("Você já tentou essa letra.")
        letra = input("Adivinhe outra letra: ").lower()
    
   
    letras_adivinhadas.append(letra)
    
   
    if letra not in palavra_secreta:
        tentativas += 1
        print("Errado! Tente novamente.")
    else:
     
        nova_palavra_mostrada = ""
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra or palavra_mostrada[i] != "_":
                nova_palavra_mostrada += palavra_secreta[i]
            else:
                nova_palavra_mostrada += "_"
        palavra_mostrada = nova_palavra_mostrada


if "_" not in palavra_mostrada:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
