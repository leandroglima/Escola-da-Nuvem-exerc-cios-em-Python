# Exercicio 18 - Verificador de Palíndromo

def eh_palindromo(texto: str) -> bool:
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

# Programa principal
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)

if resultado:
    print("Sim, é um palíndromo!")
else:
    print("Não, não é um palíndromo.")
