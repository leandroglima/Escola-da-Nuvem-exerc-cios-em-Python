# Calculadora de IMC (Índice de Massa Corporal)

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 35:
    classificacao = "Peso normal"
elif imc < 50:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.2f} — Classificação: {classificacao}")