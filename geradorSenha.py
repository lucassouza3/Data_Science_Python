import random
import string
size = int(str(input('Qual o tamanho da senha que você deseja? ')).strip()) 
#Boas prátias = senhas a partir de 16 caracteres
chars = string.ascii_letters + string.digits + '!.@%()-=+,:/\'' 
'''Stringg.ascii_letters = gera na senha letras maiúsculas e minúsculas. Também há o UpperCase e o LowerCase
String.digits = de 0 a 9, apenas numerais.'''
rnd = random.SystemRandom()
'''SystemRandon utiliza a classe urandom e gera números aleatórios a partir de fontes fornecidas pelo S.O'''
print(''.join(rnd.choice(chars) for i in range(size)))