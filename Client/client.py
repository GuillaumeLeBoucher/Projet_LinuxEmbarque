import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)

monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


buf = ''
while len(buf)<4:
    buf += monSocket.recv(4-len(buf))
size = struct.unpack('!i', buf)
print ("receiving %s bytes" % size)


with open('tst.jpg', 'wb') as img:
    while True:
 
        # saisie de la requête au clavier et suppression des espaces des 2 côtés
        requete = input('?: ').strip()
 
        # test d'arrêt
        if requete=="":
            break
         # envoi de la requête au serveur
        monSocket.sendto("%s" % requete, (UDP_IP, UDP_PORT))
 
        # réception et affichage de la réponse
        reponse, adr = monSocket.recvfrom(buf)
        print ("=> %s" % reponse)
        data = client.recv(1024)
        if not data:
            break
        img.write(data)
    print ('received, yay!')
 
    # fermeture de la connexion
monSocket.close()

# while True:
 
#         # saisie de la requête au clavier et suppression des espaces des 2 côtés
#         requete = input('?: ').strip()
 
#         # test d'arrêt
#         if requete=="":
#             break
#          # envoi de la requête au serveur
#         monSocket.sendto("%s" % requete, (UDP_IP, UDP_PORT))
 
#         # réception et affichage de la réponse
#         reponse, adr = monSocket.recvfrom(buf)
#         print ("=> %s" % reponse)
 
#     # fermeture de la connexion
# monSocket.close()
# print ("fin du client UDP")
