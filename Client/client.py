import socket
import numpy as np
import cv2
import json

#test

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)

monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#====     Message d'initialisation au serveur ========

requete = "Init OK"
monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))
#On passe le JSON dans l'état 3, la pi est connectée, on est en attente

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


 #====  Ecriture dans le JSON a integrer dans la partie reception========

#On récupère les données du JSON existant 
with open("./App-Web/src/app/image-detail/shared/data.json", "r") as f_read:
    dico = json.load(f_read)
print(dico)
#Enregistrement du nouveau contenu au bon endroit Faire des inputs pour category, caption et name qu'on met dans l'url
NbPhotos = len(dico["PhotoPath"])
Listephotos = dico["PhotoPath"]
Listephotos.append({'id': NbPhotos+1, 'category': 'NewCat', 'caption': 'Test Json for NewCat', 'url': 'assets/img/test_01.jpg'})
dico["PhotoPath"] = Listephotos
print (dico)
#Sauvegarde (écrasement)
with open("./App-Web/src/app/image-detail/shared/data.json", "w") as f_write:
    json.dump(dico, f_write)

#====  Réception de la photo ========

# if (requete == 1):
    # on ouvre le JSON et on modifie l'état pour le passer de 0 à 1. On a envoyer une demande de photo, phase d'émission


if (requete == 2):
    #Changer l'etat dans le JSON on est dans l'état reception
    #Faire un input pour demander le nom et aller mettre la photo dans assets, img...
    # de plus on modifie l'état dans le JSON, on passe de 1 à 2, phase de reception
    msg_recu, adr = monSocket.recvfrom(500000)
    print('Image ' + ' recu' + 'taille :' + str(len(msg_recu)))
    nparr = np.fromstring(msg_recu, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('image3' + '.jpg',img_np)
    #reception terminer on repasse de 2 à 3, ou 3 est l'état en attente

#if (requete == 3):
    # On ferme la connexion, on repasse l'état de 3 à 0 dans le JSON