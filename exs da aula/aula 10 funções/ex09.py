def contar_vogais(string):
    vogais = "aeiou"
    return sum(1 for char in string.lower() if char in vogais)

texto = input("Digite uma palavra ou frase: ")

print(f"O número de vogais é: {contar_vogais(texto)}")

