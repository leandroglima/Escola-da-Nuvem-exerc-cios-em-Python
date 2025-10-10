# Exercicio 24 - Consulta de Cotação de Moeda

import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    chave = f"{moeda}BRL"
    if chave not in dados:
        print("❌ Moeda não encontrada.")
    else:
        info = dados[chave]
        print("=== Cotação Atual ===")
        print("Moeda:", moeda, "→ BRL")
        print("Valor atual: R$", info['bid'])
        print("Máxima: R$", info['high'])
        print("Mínima: R$", info['low'])
        print("Última atualização:", info['create_date'])

except requests.exceptions.RequestException:
    print("❌ Erro ao acessar a API de câmbio.")
