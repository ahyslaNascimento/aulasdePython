def inverter_string(string):
    return string[::-1]


texto = input("Digite uma palavra ou frase: ")

print(f"A string invertida é: {inverter_string(texto)}")