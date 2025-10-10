# Exercicio 23 - Consulta de Endereço via CEP

import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    if 'erro' in dados:
        print("❌ CEP não encontrado.")
    else:
        print("=== Dados do CEP ===")
        print("Logradouro:", dados['logradouro'])
        print("Bairro:", dados['bairro'])
        print("Cidade:", dados['localidade'])
        print("Estado:", dados['uf'])

except requests.exceptions.RequestException:
    print("❌ Erro ao consultar o CEP.")
