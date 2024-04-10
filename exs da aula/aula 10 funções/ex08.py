def palindromo(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


texto = input("Digite uma palavra ou frase: ")

if palindromo(texto):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
