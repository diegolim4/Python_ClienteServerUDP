import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(' Socket criado com sucesso')

host = 'localhost'
port = 5432

# Ligação cliente servidor com bind

s.bind((host, port))
msg = '\nServidor: Olá Cliente'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (msg.encode()), end)


