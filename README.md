# Projet : Linux embarqué Caméra IP basé su Raspberry pi.

# Groupe

Le groupe de projet est composé de :

* Nathan Fourniol
* Clément Bichat
* Aurélien Grenier
* Guillaume Le Boucher


## Sujet du Projet

L'intitulé du projet se situe à l'adresse suivante : [sujet](Sujet_Projet_Camera.md)

L'objectif principal va être de mettre en place une caméra IP à l'aide d'une RPI3 puis de prendre des photos avec cette dernière

## Fonctionnalités

1. Prendre une photo à distance et la visualiser

2. Avoir des informations de l'état de la caméra via une led



Vous trouverez dans ce README les sections suivantes :

- **Configuration du système :** Cette section va expliquer l'ensemble des étapes nécessaires à la configuration de notre système. Ce dernier est composé de la RPI3 et de la caméra. On y retrouvera donc une description des étapes : de la cross compilation, du flashage de la carte SD, etc...

- **Utilisation de la caméra IP :** Cette section va décrire la marche à suivre afin qu'un utilisateur puisse utiliser la caméra IP avec la RPI3




## Mise en place du système

On utilisera Buildroot pour compiler et paramétrer notre système d'exploitation embarqué.
Pour ce projet, une tarball Buidroot est disponible par l'intermédiaire d'une image Docker. Cette tarball contient l'os précompilé.

Commande pour récupérer l'image et créer le conteneur Docker :

```
sudo docker pull pblottiere/embsys-rpi3-buildroot-video
sudo docker run -it pblottiere/embsys-rpi3-buildroot-video /bin/bash

```
On peut ensuite extraire l'os :

```
cd /root
tar zxvf buildroot-precompiled-2017.08.tar.gz

```

## Flashage de la carte SD

Il faut tout d'abord sortir l'image de l'os du docker :

`docker cp <container_id>:/root/buildroot-precompiled-2017.08/output/images/sdcard.img`

Puis ensuite flasher :

`sudo dd if=sdcard.img of=/dev/sdb`

Bien vérifier le chemin de la carte SD (utilisation de lsblk)

La carte SD possède donc deux partitions. Il faut ajouter dans le fichier
`config.txt` de la première partition.

```
start_x=1
gpu_mem=128

```




## Cross compilation du serveur

On utilise les Autotools pour compiler v4l2grab.

Pour s'adapter à la cible embarquée, il faut commenter dans config.h.in la ligne #undef malloc (sinon rpl_malloc sera utilisé mais il n'existe pas sur notre OS installé sur la Raspberry). Le script configure va déterminer l'environnement et adapter ainsi précisément la compilation.
Il faut lui passer en argument le compilateur qui va générer les exécutable ainsi que la cible embarquée.

*Commande pour compiler v4l2grab :*

 `./autogen.sh`

 `./configure CC=./../buildroot-precompiled-2017.08/output/host/usr/bin/arm-linux-gcc --host=arm-linux`

 `make`


## Discutions entre le serveur et le client : communication UDP

  1. Le client se connecte au serveur
  2. Le client demande une photo
  3. Le serveur prend une photo
  4. Le serveur envoie la taille du buffer au client
  5. Le serveur envoie la photo au client

  dans imageProcess
  *on alloue de la mémoire
  *on le lit
  *fonctionne
  *ecriture
