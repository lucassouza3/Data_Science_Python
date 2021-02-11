import hashlib #implementta interface comum para muitos algoritmos de hash
a1 = 'Teste1.txt'
a2 = 'Teste2.txt'

#Gerar Hash 1
hash1 = hashlib.new('ripemd160')
hash1.update(open(a1, 'rb').read())#Faz a comparação do hash, parâmetro = frase a ser comparada
#Gerar Hash 2
hash2 = hashlib.new('ripemd160')
hash2.update(open(a2, 'rb').read())

if hash1.digest() != hash2.digest(): #A função digest resume os dados passados para o update.
    print(f'Os hashs são diferentes! \n\n\t\033[31m{a1}\033[m difere de \033[33m{a2}\033[m')
else:
    print(f'Os hashs são iguais. \n\n\t\033[31m{a1}\033[m é igual a \033[33m{a2}\033[m')

print(f'Segue os hashs: \n\t{a1} = \033[31m{hash1}\033[m \n\t{a2} = \033[33m{hash2}\033[m')