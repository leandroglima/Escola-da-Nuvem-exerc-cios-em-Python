# Exercicio 21 - Gerador de Senhas Aleatórias

import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
print("=== Gerador de Senhas ===")
tamanho = int(input("Digite o tamanho desejado para a senha: "))
senha = gerar_senha(tamanho)
print("Senha gerada:", senha)
