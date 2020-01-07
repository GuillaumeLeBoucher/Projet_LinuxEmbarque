import socket


UDP_IP = "localhost"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)
print ("Message to send: ", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
messageByte = MESSAGE.encode()
sock.sendto(messageByte, (UDP_IP, UDP_PORT))
