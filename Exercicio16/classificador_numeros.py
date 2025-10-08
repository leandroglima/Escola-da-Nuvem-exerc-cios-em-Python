# Exercicio 16 - Classificador de Números Pares e Ímpares

print("=== Classificador de Números ===")
print("Digite números inteiros. Digite 0 para encerrar.
")

pares = 0
impares = 0

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    elif numero % 2 == 0:
        pares += 1
        print("→ Número par.")
    else:
        impares += 1
        print("→ Número ímpar.")

print("\n=== Resultado Final ===")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
