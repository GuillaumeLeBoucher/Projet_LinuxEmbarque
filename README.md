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
commenter dans config.h.in la ligne #undef malloc (car sinon veut utiliser rpl_malloc mais n'existe pas pour l'os utilisé dans rasp)
configuration pour utiliser le compilateur arm-linux-gcc avec autotools pour compiler pour la rasberry pi (host) : ./configure CC=./../buildroot-precompiled-2017.08/output/host/usr/bin/arm-linux-gcc --host=arm-linux
