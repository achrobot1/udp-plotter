import matplotlib.pyplot as plt
import random
import socket
import struct

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('0.0.0.0', 4444))

print(f'Listening on port: {4444}')
print('--------------------------------------------')


plt.axis([0, 20, 0, 1])
plt.grid()

for i in range(20):
    message, address = serverSocket.recvfrom(1024)

    contents = struct.unpack('1f', message)[0]

    # plt.scatter(i, contents)

    plt.stem([i], [contents])
    plt.pause(0.2)

plt.show()
