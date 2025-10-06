# Conversor de Moeda
valor_reais = 150.50
taxa_dolar = 5.35
taxa_euro = 6.50

valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Valor convertido em dólares: US$", round(valor_em_dolar, 2))
print("Valor convertido em euros: €", round(valor_em_euro, 2))