import socket
import sys
ip='127.0.0.1'
port=3999
try:
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect((ip, port)) 
    print('Client is connected to server')
except socket.error:
    print('Unable to create connection')
    sys.exit()
data=input('Enter data to send :')
client.send(bytes (data, 'utf-8'))
while True : 
    data=client.recv(1024) 
    print(f' from Server: {data.decode()}') 
    data=input('Enter data to send :')
    client.send(bytes (data, 'utf-8'))
