#Transport control Protocol → Permite saber se os pacotes foram enviados na ordem correta.
import socket #Faz o relacionamento (Placa de Rede - Sistema Operacional)
#Socket fornece acesso de baixo nível à interface de rede.
import os 
import sys #Não se confunde com os, sys fornece variáveis e funções com forte interação com o Python
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #AF_INET → Protocolo IP; SOCK_STREAM → TCP;
    except socket.error as e:
        print('A conexão falhou.')
        print(f'Erro: {e}')
        sys.exit()
    print('Socket criado com sucesso.')
    
    hostAlvo = str(input('Qual o host a ser conectado? \n')).strip()
    portaAlvo = str(input('Qual a porta a ser conectada? \n')).strip()

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print(f'Cliente TCP conectado com sucesso! \nHost Alvo: {hostAlvo}\nPorta Alvo: {portaAlvo}')
        s.shutdown(2) #Espera 2 segundos para finalizar a conexão. Evita o Looping.

    except socket.error as e:
        print('A conexão falhou.')
        print(f'Erro: {e}')
        sys.exit()
    
if __name__ == "__main__":
    main()
