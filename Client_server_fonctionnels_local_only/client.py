import socket
import numpy as np
import cv2
import os
import inspect
import json
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)
JSON_FILE = "./../App-Web/src/app/image-detail/shared/data.json"
PATH_PREFIX = "./../App-Web/src/assets/img/"
monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

#====     Message d'initialisation au serveur ========

requete = "Init OK"
monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))

#==== Reception message de réponse du serveur ========

reponse, adr = monSocket.recvfrom(1024)
print("Reponse serveur : ", reponse)

#modifier le Json pour communique l'etat de la connection au serveur
with open(JSON_FILE, "r") as f:
    dico = json.load(f)
    dico["Etat"] = "1"
with open(JSON_FILE, "w") as f:
    json.dump(dico, f)

#Fonctions

def sendRequest(buf):
    """Envoie le contenu de buff au serveur 
    """
    monSocket.sendto(buf.encode(), (UDP_IP, UDP_PORT))
    
def receiveImage(name):
    """
    Reception de l'image
    """
    msg_recu, adr = monSocket.recvfrom(500000)
    print('Image recu taille : ', str(len(msg_recu)))
    nparr = np.fromstring(msg_recu, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(PATH_PREFIX + name +'.jpg',img_np)     

def veille():
    input_client = "0"
    while input_client != "1":
        input_client = input(" Quelle commande voulez-vous ?:\n Entrée 1 pour prendre une photos et l'envoyer vers votre gallerie ").strip()  


    with open(JSON_FILE, "r") as f:
        dico = json.load(f)
    
    #send msg to serveur :
    sendRequest("1")
    NbPhotos = len(dico["PhotoPath"])
    pictName = input("Entrer un nom pour votre photo ")
    if not pictName :
        pictName = "image" + str(NbPhotos + 1)
    pictDescription = input("Entrez une description pous votre photo (obtionnel faites entrer sinon)")
    if not pictDescription:
        pictDescription = "Pas de description"
    receiveImage(pictName)
    dico["PhotoPath"].append({'id': NbPhotos+1, 'caption': pictDescription, 'url': 'assets/img/' + pictName + '.jpg'})
    
    with open(JSON_FILE, "w") as f:
        json.dump(dico, f)

if __name__ == "__main__" :
    veille()

#==== Saisie de la requête au clavier et suppression des espaces des 2 côtés

  
        
#requete = input(' Quelle commande voulez-vous ?: ').strip()
#print("Ordre serveur : ",requete)
#monSocket.sendto(requete.encode(), (UDP_IP, UDP_PORT))

# réception et affichage de la réponse
#buf_size, adr = monSocket.recvfrom(1024)
#print("Reponse socket")
#print ("=> %s" % buf_size)

#====  Réception de la photo ========

#if (requete == "2"): 
#    msg_recu, adr = monSocket.recvfrom(500000)
#    print('Image ' + ' recu' + 'taille :' + str(len(msg_recu)))
#    nparr = np.fromstring(msg_recu, np.uint8)
#    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#    cv2.imwrite('./../App-Web/src/assets/img/image3' + '.jpg',img_np)
