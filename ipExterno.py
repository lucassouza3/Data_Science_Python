import re #Permite operações com expressões regulares
import json #codificação e decodificação JSON
from urllib.request import urlopen
url = 'https://ipinfo.io/json' #Recebe url do site com a url externa
resposta = urlopen(url) #Dados do url vão para resposta
dados = json.load(resposta) #JSON carrega todo o JS e envia para a variável dados
ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
regiao = dados['region']
print('Detalhes do IP externo')
print(f'IP: {ip}\nPaís: {country}\nEstado: {regiao}\nCidade: {city}\nProvedor de Internet: {org}')