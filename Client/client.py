import socket
import numpy as np
import cv2

#test

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)

monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#====     Message d'initialisation au serveur ========

requete = "Init OK"
monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))

#==== Reception message de réponse du serveur ========

reponse, adr = monSocket.recvfrom(1024)
print("Reponse serveur : ", reponse)

#==== Saisie de la requête au clavier et suppression des espaces des 2 côtés

requete = input(' Quelle commande voulez-vous ?: ').strip()
print("Ordre serveur : ",requete)
monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))

# réception et affichage de la réponse
#buf_size, adr = monSocket.recvfrom(1024)
#print("Reponse socket")
#print ("=> %s" % buf_size)

#====  Réception de la photo ========

if (requete == 2):
    msg_recu, adr = monSocket.recvfrom(500000)
    print('Image ' + ' recu' + 'taille :' + str(len(msg_recu)))
    nparr = np.fromstring(msg_recu, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('image3' + '.jpg',img_np)
