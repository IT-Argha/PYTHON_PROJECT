import socket
import sys
try:
    server=socket.socket()
    ip='127.0.0.1'
    port=3999
    server.bind((ip, port))
    server.listen(1)
    print('Server is listening....')
except socket.error: 
    print('Unable to create socket')
    sys.exit()
while True:
    client, addr=server.accept() # Connection established
    print (f'Client from {addr} is connected...')
    break
while True:
    data=client.recv(1024) 
    print(f' from Server: {data.decode()}') 
    data=input('Enter data to send :')
    client.send(bytes (data, 'utf-8'))

 
