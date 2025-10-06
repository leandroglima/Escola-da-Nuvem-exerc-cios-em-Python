idade = int(input("Digite sua idade: "))

if 0 <= idade <= 10:
    categoria = "Criança"
elif 12 <= idade <= 15:
    categoria = "Adolescente"
elif 16 <= idade <= 49:
    categoria = "Adulto"
elif idade >= 65:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

print("Você é classificado como:", categoria)