import requests
from config import URL_BASE, API_KEY

nome_cidade = input("Insira o nome da cidade para pesquisar o clima: ")

# q={city name}&appid={API key}
url_completa = f"{URL_BASE}q={nome_cidade}&appid={API_KEY}"
print(url_completa)

dados_recebidos = requests.get(url_completa).json()
print(dados_recebidos)

if dados_recebidos['cod'] != '404':
    #dados da chave "main"
    principal = dados_recebidos['main']
    print(principal)
    temperatura_corrente = principal["temp"]
    pressao_corrente = principal['pressure']
    umidade_corrente = principal['himidity']

    #Dados da chave "weather"
    clima = dados_recebidos['weather']
    print(clima)
    descrica_clima = clima['description']


else:
    print("Cidade não encontrada")