import hashlib
def menu():
    print('#'*35)
    print('Bem vindo ao Gerador de Hash\nQual tipo de Hash deseja gerar?\n[1]MD5\n[2]SHA1\n[3]SHA256\n[4]SHA512\n[0]SAIR')
    print('#'*35)
    opcao = int(input(''))
    print('#'*35)
    return opcao

def menuescolha(escolha):
    while True:
        if escolha == 0:
            print('Obrigado!')
            break
        elif escolha == 1:
            texto = str(input('Digite a frase a ser convertida: ')).strip()
            resultado = hashlib.md5(bytes(texto,'utf-8')) #Bytes converte string em bytes. UTF-8 permite o uso do acento.
            char = len(resultado.hexdigest())
            print(f'O hash da string é: {resultado.hexdigest()}.\nE ele possui {char} caracteres.')
            break
        elif escolha == 2:
            texto = str(input('Digite a frase a ser convertida: ')).strip()
            resultado = hashlib.sha1(bytes(texto, 'utf-8'))
            char = len(resultado.hexdigest())
            print(f'O hash da string é: {resultado.hexdigest()}.\nE ele possui {char} caracteres.')
            break
        elif escolha == 3:
            texto = str(input('Digite a frase a ser convertida: ')).strip()
            resultado = hashlib.sha256(bytes(texto, 'utf-8'))
            char = len(resultado.hexdigest())
            print(f'O hash da string é: {resultado.hexdigest()}.\nE ele possui {char} caracteres.')
            break
        elif escolha == 4:
            texto = str(input('Digite a frase a ser convertida: ')).strip()
            resultado = hashlib.sha512(bytes(texto, 'utf-8'))
            char = len(resultado.hexdigest())
            print(f'O hash da string é: {resultado.hexdigest()}.\nE ele possui {char} caracteres.')
            break
        else: 
            print('Favor digitar uma opção válida.')
            break
x = menu()
menuescolha(x)