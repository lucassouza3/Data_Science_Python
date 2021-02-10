#User Datagram Protocol mais veloz que o TCP, porém, não há garantia de que o pacote chegou com sucesso.
import socket
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente socket criado com sucesso.')
host = 'localhost'
porta = 5433
mensagem = str(input('Digite uma mensagem: ')).strip()
try:
    print(f'Cliente: {mensagem}')
    connect.sendto(mensagem.encode(), (host, 5433))
    dados, servidor = connect.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print(f'Cliente: Fechando a conexão')
    connect.close()
