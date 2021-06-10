import socket

# objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket criado com sucesso!')

host = 'localhost:'
port = 5433
msg = 'Olá Servidor!'

# enviar e receber a mensagem
try:
    print(f'Cliente {msg}')
    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)  # 4096 Bytes
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
