def palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    texto_limpo == texto_limpo[::-1]
    return "é palindromo"


def contador_de_vogais(texto):
    vogais = 'aeiouAEIOU'
    return sum(1 for letra in texto if letra in vogais)

def inverter_string(texto):
    return texto[::-1]
