import os #importa módulo Operacional System, a qual integra os programas e recursos do S.O.
print("><"*30)
ipHost = str(input('Digite o IP ou Host a ser verificado: ')).strip()
print("><"*30)
os.system(f'ping -n 6 {ipHost}') #Acessa a biblioteca os e inicia o ping, e passando a variável pedida como parâmero.

