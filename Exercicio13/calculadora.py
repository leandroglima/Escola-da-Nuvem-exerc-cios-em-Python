# Exercicio 13 - Calculadora com operações básicas

print("=== Calculadora Básica ===")
print("Escolha a operação: +  -  *  /")

numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada: ")
numero2 = float(input("Digite o segundo número: "))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)
