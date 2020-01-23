import socket

"""Taille paquet 512"""


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)

monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
requete = "Init OK"
monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))



truc = open("toto.jpg", "wb")
i=0
while (i<62):
    reponse, adr = monSocket.recvfrom(512)
    print("Reponse serveur : ", i)
    truc.write(bytes(reponse))
    i += 1

truc.close()
monSocket.close()


"""
with open('tst.jpg', 'wb') as img:

# saisie de la requête au clavier et suppression des espaces des 2 côtés
    requete = input('?: ').strip()
    #print(requete)
    #print(requete.encode())
    # test d'arrêt
    # envoi de la requête au serveur
    monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))

    # réception et affichage de la réponse
    buf_size, adr = monSocket.recvfrom(1024)
    print("Reponse socket")
    print ("=> %s" % buf_size)

    image, adr = monSocket.recvfrom(int(512))
    print("Image :", image)
    end = ""


    while(end !="END FILE"):
        #requete = input('?: ')
        #if requete == "q":
            #break
        data, adr = monSocket.recvfrom(int(512))
        try :
            print(data.decode("utf-8"))
            end = data.decode("utf-8")
        except:
            print(data)
        truc.write(bytes(data))
        image = image + data
        #print("Image ajout", image)
    print ('received, yay!')

    print("FIN envoie")
    truc.close()
    img.write(bytes(image))

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
"""
