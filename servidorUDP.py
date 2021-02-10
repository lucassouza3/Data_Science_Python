import socket
import os
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')
host = 'localhost'
porta = 5432
connect.bind((host,porta)) #Liga cliente/servidor através da porta.
mensagem = str(input('Digite sua mensagem: ')).strip()

while True:
    dados, endereço = connect.recvfrom(4096)
    if dados == True:
        print('Servidor enviando mensagem...')
        connect.sendto(dados + (mensagem.encode()), endereço)