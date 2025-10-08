# Exercicio 19 - Cálculo de Desconto em Produto

def calcular_desconto(preco: float, percentual: float) -> float:
    valor_desconto = preco * (percentual / 100)
    return valor_desconto

def preco_final(preco: float, desconto: float) -> float:
    return preco - desconto

# Programa principal
preco = float(input("Digite o preço do produto (R$): "))
percentual = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = calcular_desconto(preco, percentual)
preco_com_desconto = preco_final(preco, valor_desconto)

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final do produto: R$ {preco_com_desconto:.2f}")
