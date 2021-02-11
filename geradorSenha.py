import random
import string
from time import sleep
def password():
    size = int(str(input('Qual o tamanho da senha que você deseja? ')).strip()) 
    #Boas práticas = senhas a partir de 16 caracteres
    chars = string.ascii_letters + string.digits + '!.@%()-=+,:/\'' 
    '''Stringg.ascii_letters = gera na senha letras maiúsculas e minúsculas. Também há o UpperCase e o LowerCase
    String.digits = de 0 a 9, apenas numerais.'''
    rnd = random.SystemRandom()
    '''SystemRandon utiliza a classe urandom e gera números aleatórios a partir de fontes fornecidas pelo S.O'''
    print(''.join(rnd.choice(chars) for i in range(size)))

def menu():
    count = 0
    while True:
        print('[1]Gerar Senha\n[2]Sair do programa')
        m = int(str(input('')).strip())
        if m == 1:
            password()
        elif m == 2:
            break
        else:
            print('\033[31mAtenção, há apenas 2 opções.\033[m')
            count += 1
        if count == 3:
            print('\033[31mO programa será fechado.\033[m')
            sleep(2)
            break

#Início
menu()