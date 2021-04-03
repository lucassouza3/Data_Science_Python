####INCOMPLETO######

#Utilizado em datamining ou data science, para levantar informações em um processo de pentest
from bs4 import BeautifulSoup
import operator
from collections import Counter
import requests

def start(url):
    worldlist = [] #Lista vazia
    source_code = requests.get(url).text
    print(source_code)
    soup = BeautifulSoup(source_code, 'html.parser')
    for cadaTexto in soup.findAll('div', {'class': 'entry-content'}):
        conteudo = cadaTexto
        print(conteudo)
        words = conteudo.lower().split()
        
        for cadaPalavra in words:
            worldlist.append(cadaPalavra)
           

    listaLimpa(worldlist)

def listaLimpa(worldlist):
    listaLimpa = []
    for w in worldlist:
        symbols = '!@#%¨&*()-+<>?/., ' #Símbolos indesejados
        for i in range(0,len(symbols)):
            w = word.replace(symbols[i],'') #Troca o símbolo por '' vazio
        if len(w) > 0:
            listaLimpa.append(w)
    criarDicionario(listaLimpa)

def criarDicionario(listaLimpa):
    contarPalavras = {}
    for w in listaLimpa:
        if w in contarPalavras:
            contarPalavras[w] += 1
        else:
            contarPalavras[w] = 1
    for key, value in sorted(contarPalavras.items(), key = operator.itemgetter(1)):
        print('% s : % s' % (key, value))
    c = Counter(contarPalavras)
    top = c.most_common(10)
    print(top)


#site = str(input('URL do site: ')).strip().lower()
start('https://www.google.com')
#start('https://'+ site)