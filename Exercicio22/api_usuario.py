# Exercicio 22 - Consulta de Usuário Fictício via API

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()
    dados = resposta.json()

    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("=== Usuário Aleatório ===")
    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("❌ Falha ao acessar a API.")
