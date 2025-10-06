# Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 150.00
porcentagem_desconto = 10  # em %

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final com desconto: R$", round(preco_final, 2))