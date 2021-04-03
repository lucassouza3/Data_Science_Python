#Criando um gerador de world list :p
import itertools
from time import sleep
lista = []
string = str(input('Texto a ser permutado: ')).strip()
resultado = itertools.permutations(string) #OK
for i in resultado:
    lista.append(''.join(i))
print(len(lista))
print(lista)
