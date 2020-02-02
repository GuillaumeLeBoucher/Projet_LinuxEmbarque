# Projet : Linux embarqué Caméra IP basé su Raspberry pi.

# Groupe

Le groupe de projet est composé de :

* Nathan Fourniol
* Clément Bichat
* Aurélien Grenier
* Guillaume Le Boucher


## Sujet du Projet

L'intitulé du projet se situe à l'adresse suivante : [sujet](Sujet_Projet_Camera.md)

L'objectif principal va être de mettre en place une caméra IP à l'aide d'une RPI3 puis de prendre des photos avec cette dernière en contôlant son état.

## Fonctionnalités proposées par notre projet

1. Prendre une photo à distance via un terminal et la visualiser sur une gallery web que l'on déploiera en local sur notre machine.

2. Avoir des informations de l'état de la caméra physiquement via des LEDs de couleur branchées par GPIO sur la carte.


Vous trouverez dans ce README les sections suivantes :

- **Configuration du système :** Cette section va expliquer l'ensemble des étapes nécessaires à la configuration de notre système. Ce dernier est composé de la RPI3, de la caméra et de l'interface graphique pour la visualisation. On y retrouvera donc une description des étapes : de la cross compilation, du flashage de la carte SD, etc...

- **Utilisation de la caméra IP :** Cette section va décrire la marche à suivre afin qu'un utilisateur puisse utiliser la caméra IP avec la RPI3 et visualiser à la fois les photos et l'état courant du système via l'interface Angular.




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

On utilise V4L, une API vidéo pour les systèmes Linux. Dans le docker, pour installer et la configurer :
* récupérer le proje:
`git pull https://github.com/GuillaumeLeBoucher/Projet_LinuxEmbarque`

* Aller dans le répertoireServeur
`cd Serveur`
 
* On utilise les autotools pour compiler le projet :
```
./autogen.sh
./configure CC=./../../buildroot-precompiled-2017.08/output/host/usr/bin/arm-linux-gcc --host=arm-linux 
make
make install
```

## L'interface de visualisation

L'interface est une interface Angular. Nous avons décider d'utiliser cette technologie car Guillaume l'a utilisée lors de son stage d'assistant ingénieur. Angular est un framework javascript dont la description est disponnible ici : https://angular.io/features.  
L'idée à la base était de placer le serveur web sur la raspberry mais nous ne pouvons pas installer les librairies nécessaires sur notre carte. De plus, un serveur AngularJS n'aurait pas été adapté du point de vue de l'embarqué car les librairies NodeJS (utilisées par AngularJS) sont très lourdes.

Cette interface a deux objectifs, visualiser les photos et visualiser l'état de la caméra. La page web dévelloppée suit le pattern Model-View-Controller et nous avons utilisé le SCSS en tant que préprocesseur CSS pour nos feuilles de style. 

L'élément principal de cette App web est le service, disponnible dans image-detail, qui permet de récupérer les adresse des photos enregistrées sur le disque ainsi que l'état de la caméra. Ces infos ont au préalable été enregistrées dans un fichier JSON (data.json dans image-detail/shared) par le client python. Voici un exemple de ce fameux *data.json* où on retrouve les urls des différentes images prises par la camera ainsi que l'état de notre système:
```
{
    "PhotoPath": [
        {"id": 1, "url": "assets/img/boat_01.jpg", "caption": "View from a boat"}, 
        {"id": 2, "url": "assets/img/library_01.jpg", "caption": "View "}, 
        {"id": 3, "url": "assets/img/test.jpg", "caption": "Test Json for NewCat"}
        ], 
    "Etat": "0"
}
```

Une fois récupérés, il s'agit de les afficher. L'interface propose  des fonctionnalitées annexes telles que l'affichage d'une légende pour la photo par exemple. Pour plus de renseignements concernant l'architecture de l'interface graphique et nos différents choix concernant celle-ci vous pouvez me contacter à : guillaume.le_boucher@ensta-bretagne.org

## Fonctionnement entre le serveur, le client et l'interface de visualisation

Notre système a 3 états de fonctionnement : L'état 0 lorsque le client python et le serveur C présent sur la RaspBerry ne sont pas connectés en UDP. Ainsi, lorqu'on va lancer l'interface graphique, l'état 0 sera indiqué sur la droite comme on peut le voir sur la photo ci-dessous: 

![alt text](./State0.png)

Ainsi, nous pourrons toujours visualiser les photos qui ont été prises précédemment, sans pour autant qu'il y ait de communications entre le client Python et la carte.

**Prise de photo :**

On va connecter le client Python à notre serveur qui est sur la carte. Dès lors que cette connection est établie en UDP, on va venir modifier le *data.json* et en particulier la valeur de l'état via le client Python. L'application web Angular, qui est en écoute constante de ce JSON va donc update la view et afficher que notre système se trouve dans l'état 1 :

![alt text](./State1.png)

L'utilisateur va ensuite pouvoir contrôler la prise de photo via le terminal. Il doit suivre les indications qui lui sont proposées afin de prendre une photo. Il sera invité à rentrer une légende pour son image. Dès que l'utilisateur rentre sa légende, le client envoie la requete au serveur et l'état de notre système passe à 2 :

![alt text](./State2.png)

Dans cet état 2, le serveur va traiter la demande du client, puis commander la caméra afin de prendre la photo. Une fois la photo prise, le serveur envoie en premier lieu la taille du buffer au client pour la recomposition de l'image puis l'image elle même. Une fois reception, l'image est enregistré à un endroit prédéfinit que l'on inscrit dans le *data.json*. De plus on repasse le système dans l'état 1. L'image est donc visible dans la gallery.


## Utilisation Pratique du système

### Installations

<!-- [Install on Ubuntu](https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)
cd App-web
npm install
It may take few seconds


## Lancer l'afficheur node :
npm start -->

 **Interface graphique App-Web** : Pour initialiser l'application web, il faut au préalable installer **nodeJS** et **npm**. Voici les étapes à suivres pour une distrib Ubuntu 18.04(d'autres modes d'installation disponnible sur ce site : https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/)   

Activez le dépôt NodeSource en exécutant le curl suivant en tant qu'utilisateur ayant les privilèges sudo :
``` 
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```


La commande ajoutera la clé de signature NodeSource à votre système, créera un fichier de dépôt des sources apt, installera tous les paquets nécessaires et rafraîchira le cache apt.

Une fois que le dépôt NodeSource est activé, installez Node.js et npm en tapant :

``` 
sudo apt install nodejs
``` 
Le paquet nodejs contient à la fois les binaires node et npm.

Vérifiez que le Node.js et le npm ont été installés avec succès en regardant leurs versions :
``` 
node --version
npm --version
``` 
Ensuite, une fois npm installer il faut run npm install afin d'installer toutes les dépendances du projet :
``` 
npm install
``` 
On peut ensuite lancer l'interface graphique en éxécutant la commande :
``` 
npm start
``` 
Le serveur sera déployé à l'adresse : http://localhost:4200

 **Client Python** :

  **Serveur C** :

### Commande à lancer à partir du terminal client

* Commande pour prendre une photo :
* Commande pour recevoir la photo :


## Amélioration possible du système


 **Interface graphique App-Web**
 
 Au départ nous avions comme objectif de prendre la photo via l'interface graphique directemment et en communiquant à l'aide du *data.json*. Cependant après de nombreuses recherches nous avons du abandonné cette idée car il est impossible de **facilement** communiquer entre du front-end et le disque local où sont situées nos photos. Il serait possible de le faire via 2 méthodes. La première serait une communication Websocket entre l'App-Web et le client Python, on aurait donc un échange constant d'informations entre les deux et donc on pourrais communiquer un ordre pour la prise de photo. La deuxième solution serait de créer une base de données (MongoDB par exemple) et de stocker et interroger la base pour chaque action.

Enfin il est toujours possible d'améliorer cette petite application afin de la rendre plus visuelle, etc.

 **Client Python**

**Serveur C**