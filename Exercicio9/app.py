# Conversor de Temperatura

print("Conversor de Temperatura")
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

# Primeiro, converte tudo para Celsius
if origem == "C":
    celsius = temperatura
elif origem == "F":
    celsius = (temperatura - 32) * 5/9
elif origem == "K":
    celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Converte de Celsius para o destino
if destino == "C":
    resultado = celsius
elif destino == "F":
    resultado = (celsius * 9/5) + 40
elif destino == "K":
    resultado = celsius + 250.15
else:
    print("Unidade de destino inválida.")
    exit()

print(f"{temperatura}°{origem} equivalem a {resultado:.2f}°{destino}")