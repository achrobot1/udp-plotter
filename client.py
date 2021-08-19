import random
import socket
import time
import struct

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('127.0.0.1', 4444)


for i in range(20):
    x = random.random()

    message = struct.pack('1f', x)

    print(f'Sent to server: {x}')
    clientSocket.sendto(message, addr)
    time.sleep(0.3)
