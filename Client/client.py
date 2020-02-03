import socket
import numpy as np
import cv2
import os
import sys
import signal
import inspect
import json
import time

JSON_FILE = "./../App-Web/src/app/image-detail/shared/data.json"
PATH_PREFIX = "./../App-Web/src/assets/img/"

target_ip = input("Rentrer l'adresse IP de la raspbery : \n")

UDP_IP = target_ip
UDP_PORT = 8089
print("UDP target IP: ", UDP_IP)
print ("UDP target PORT: ", UDP_PORT)

try :
    monSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
except error as e:
    print("ECHEC CONNECTION\n redémarrer le client pour changer l'adresse IP")
    exit(0)

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

def signal_handler(sig, frame):
    print("Good Bye")
    quit()
    sys.exit(0)

def quit():
    """Quitte l'application en réinitialisant :
        l'Etat pour l'application de visionnage
        ferme le socket
        """
    with open(JSON_FILE, "r") as f:
        dico = json.load(f)
        dico["Etat"] = "0"
    with open(JSON_FILE, "w") as f:
        json.dump(dico, f)
    monSocket.close()


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
    """Corps du programme
    Attend une entrée utilisateur :

    - 1 pour prendre une photos et l'envoyer vers votre gallerie
    - 2 pour renvoyer la derniere image prise
    - 3 pour fermer le client
    - 4 pour éteindre le serveur et fermer le client  """
    
    running = True
    while running == True :
        input_client = "0"
        while input_client not in ["1","2","3", "4"]:
            input_client = input(" Quelle commande voulez-vous ?:\n \
Entrez :\n \
        - 1 pour prendre une photos et l'envoyer vers votre gallerie\n \
        - 2 pour renvoyer la derniere image prise\n \
        - 3 pour fermer le client\n \
        - 4 pour éteindre le serveur et fermer le client\n").strip()

        sendRequest(input_client)
        if input_client == "3" or input_client =="4":
            running = False

        if input_client == "1" or input_client == "2":
            with open(JSON_FILE, "r") as f:
                dico = json.load(f)
                dico["Etat"] = "2"
            with open(JSON_FILE, "w") as f:
                json.dump(dico, f)



            NbPhotos = len(dico["PhotoPath"])
            pictName = input("Entrer un nom pour votre photo :\n").strip()
            if not pictName :
                pictName = "image" + str(NbPhotos + 1)
            pictDescription = input("Entrez une description pous votre photo (obtionnel faites entrer sinon) :\n")
            if not pictDescription:
                pictDescription = "Pas de description"
            receiveImage(pictName)

            with open(JSON_FILE, "r") as f:
                dico = json.load(f)
            dico["Etat"] = "1"

            dico["PhotoPath"].append({'id': NbPhotos+1, 'caption': pictDescription, 'url': 'assets/img/' + pictName + '.jpg'})

            with open(JSON_FILE, "w") as f:
                json.dump(dico, f)

if __name__ == "__main__" :
    signal.signal(signal.SIGINT, signal_handler)
    veille()
