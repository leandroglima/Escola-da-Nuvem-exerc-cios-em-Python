
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 50 != 0) or (ano % 500 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")