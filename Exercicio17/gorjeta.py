# Exercicio 17 - Cálculo de Gorjeta

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Programa principal
valor_conta = float(input("Digite o valor total da conta (R$): "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")
