# Projet_LinuxEmbarque

## Sujet du Projet

L'intitulé du projet se situe à l'adresse suivante : [sujet](Sujet_Projet_Camera.md)

L'objectif principal va être de mettre en place une caméra IP à l'aide d'une RPI3 puis de prendre des photos avec cette dernière.


Le groupe de projet est composé de :

* Nathan Fourniol
* Clément Bichat
* Aurélien Grenier
* Guillaume Le Boucher

Vous trouverez dans ce README les sections suivantes :

- **Configuration du système :** Cette section va expliquer l'ensemble des étapes nécéssaires à la configuration de notre système. Ce dernier est composé de la RPI3 et de la caméra. On y retrouvera donc une description des étapes de configurations de l'IP statique, du flashage de la carte SD, etc.

- **Mode de fonctionnement de notre projet :** Cette section va décrire le mode de fonctionnement de notre système et la marche à suivre afin qu'un utilisateur quelconque utilise la caméra IP avec la RPI3


## Compilation de v4l2grab

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
