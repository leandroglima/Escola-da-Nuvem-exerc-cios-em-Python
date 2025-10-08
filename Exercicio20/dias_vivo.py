# Exercicio 20 - Cálculo de Dias de Vida

from datetime import datetime

print("=== Cálculo de Dias de Vida ===")
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.now()

dias_vividos = (data_atual - data_nasc).days

print(f"Você já viveu aproximadamente {dias_vividos} dias!")
