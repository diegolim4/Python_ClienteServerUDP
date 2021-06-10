import socket

# objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket criado com sucesso!')

host = 'localhost:'
port = 5433
msg = 'Olá Servidor!'
