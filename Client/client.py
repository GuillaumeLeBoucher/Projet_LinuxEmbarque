import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
buf = 1024
print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)
print ("Message to send: ", MESSAGE)

monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

while True:
 
        # saisie de la requête au clavier et suppression des espaces des 2 côtés
        requete = input('?: ').strip()
        print(requete)
        print(requete.encode())
        # test d'arrêt
        if requete=="":
            break
         # envoi de la requête au serveur
        monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))
 
        # réception et affichage de la réponse
        reponse, adr = monSocket.recvfrom(buf)
        print ("=> %s" % reponse)
 
    # fermeture de la connexion
monSocket.close()
print ("fin du client UDP")
# messageByte = MESSAGE.encode()
