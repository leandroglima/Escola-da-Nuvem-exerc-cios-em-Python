# Exercicio 15 - Verificador de Senha Segura

senha = input("Digite uma senha: ")

tem_oito_caracteres = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_oito_caracteres and tem_numero:
    print("✅ Senha segura!")
else:
    print("❌ Senha insegura!")
    if not tem_oito_caracteres:
        print("- A senha deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- A senha deve conter pelo menos um número.")
