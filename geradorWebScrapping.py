#Web Scrapper é uma >ferramenta de coleta de dados web<. Permite a extração de dados de sites da web
#convertendo-os em informação >estruturada< para posterior análise.
import requests
from bs4 import BeautifulSoup
urls = str(input('Digite o site a ser utilizado: ')).strip().lower()
site = requests.get('https://' + urls).content #Site recebe conteúdo da requisição http
soup = BeautifulSoup(site, 'html.parser') #Soup 'baixa' do instagram seu código html 
print(soup.prettify()) #prettify transforma o html em string e o print exibe o html.
#variavel = soup.find('<tag>', class_='<nm_class>') encontra e retorna a informação na tag e classe utilizadas