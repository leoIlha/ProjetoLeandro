import logging

import requests
import re
import json
import random

prices = []
url = "https://books.toscrape.com/"

try:
    response = requests.get(url)
    content = response.content.decode('utf-8')
except Exception as e:
    print(f"Erro ao fazer requisição: {e}")
    exit()

prices = re.findall(r'\d+\.\d{2}', content)
print(prices)
data = {"prices": prices}
try:
    with open("prices.json", "w") as f:
        json.dump(data, f)
except Exception as e:
    print(f"Erro ao salvar arquivo: {e}")
    exit()

try:
    with open("prices.json") as f:
        Sim = 'sim'
        Nao = 'nao'
        opcoes = [Sim, Nao]
        escolha = random.choice(opcoes)
        print(escolha)
    if (escolha == Nao):
        data = json.load(f)
    novalista = data["prices"]
    # seleciona um número aleatório da lista
    aleatorio = random.choice(novalista)
    print("numero escolhido da lista:", aleatorio)
    posicao = novalista.index(aleatorio)
    print("posicao do numero escolhido:", posicao)
    num = random.uniform(10, 30)
    num = format(round(num, 2), ".2f")
    print("novo numero:", num)
    novalista[posicao] = num
    print('lista com o novo valor:', novalista)
    print('Preço Alterado')
    data = {"novoprices": novalista}
    try:
        with open("novoprices.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        exit()
    print("---------------------------------")
except:
    print('Nenhum Preço Alterado')

# if(prices[posicao]!=novalista[posicao]):
#     print("Preço Alterado")
# else:
#     print("Preço continua o mesmo")
