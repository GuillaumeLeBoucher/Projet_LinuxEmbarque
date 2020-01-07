


**Compte-Rendu : projet sur Raspberry pi 3**
===========================================

## Partie 1 : Construction d'un OS avec Buildroot et une chaine de cross-compilation

On télécharge tout d'abord la BSP (Board support package) basé sur buildroot et conçu pour le TP.
Buildroot est un outils facilitant la compilation d'un OS embarqué.
Il va nous permettre de compiler :
* la toolchaine : outils qui vont nous permettre d'avoir un environnement de cross-compilation (compilateur + linker + assembleur).
* la bootloader
* le noyau linux
* le rootfs :

### Question 1 : fichiers de comfigurations

Dans cette BSP, on trouve en plus :
*  un fichier de configuration *configs/embsys_defconfig* pour la configuration de Buildroot.
* un fichier de configuration *busybox.config*. Ce fichier nous permet de configuer BusyBox, Busybox est une bibliothèque fournissant les petits outils applicatifs que l'utilisateur a rapidement besoin (bash, ls, cp...). On configure BusyBox via la commande `make busybox-menuconfig`.
* un fichier *users.tables* décrivant les utilisateurs cibles.

### Question 2 : fichier de configuration Raspberry

Comme la cible est un Raspberry avec un OS 32 bits, on trouve dans le répertoire configs la fichier de configuration Buildroot : *raspberrypi3embsys_defconfigmake*

### Question 3 : répertoire *package*

Le répertoire *package* contient les dossiers contenant des applications que l'on peut être amenées à installer dans notre build. Chacun de ces dossiers contient les fichiers de configuration des applications

### Question 4 : `make embsys_defconfig`

Buildroot intégre un système de "templates" permettant de configurer le noyau rapidement et de l'adapter à la cible.
Cette commande  permet de configurer les paramètres par défaut avec les configuration de la cible ARCH définie (ici à partir du fichier *raspberrypi3embsys_defconfigmake*).
La commande `make menuconfig` permet ensuite de lancer l'utilitaire de configuration du noyau (configuration déjà partielle avec le `make defconfig`) pour affiner la configuration. On retrouve cette configuration dans le fichier .config. (On passe par une interface graphique avec les différentes commandes make, il est assez fastidieux de modifier les différents paramètres dans le fichier directement.)

On peut ensuite configurer la compilation du noyau via la commande `make linux-menuconfig`.

On peut sauvegarder nos configuration via la commande `make linux-savedefconfig`

### Question 5 : paramètres

- l'architecture matérielle cible : ARM little
- le CPU ciblé  : Cortex A53
- l'ABI: EABIhf (target)
- la librairie C utilisée : ulibC
- la version du cross-compilateur : gcc 6 6.X
- la version du kernel : kernel version 4.19

### Question 6 : compilaion du packet `openssh`

On observe dans BR2_PACKAGE_OPENSSH que ce packet sera compilé
(location : target package / networking applications)

### Question 7 : BusyBox

Framework implémentant les commandes standards. Voir réponses précédentes.

### Question 8 : répertoire `/output`

Dans le répertoire `/output`, on trouve les fihiers en sortie de buidroot, c'est à dire les fichiers binaires destinés à la machine hôte et la toolchains.

* `/output/image` : binaire du kernel, de l'OS et des différents paquets
* `/output/host` : la toolchaine

On retrouve ainsi dans */output/host/usr/bin* le binaire du compilateur gcc compilé pour un processeur arm

### Question 9

on exécute ./hw et cela fonctionne. La compilation a fonctionné.


### Question 10

On ne peut pas éxécuter, car nous n'avons pas une architecture arm.

    hw: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-uClibc.so.0, not stripped

On remarque que la binaire est destiné à un système 32-bit LSb executable ARM...

De plus, l'interpréteur est uclibs c'est ce que l'on va installer sur le Raspberry.

### Question 11 : répertoire *output/image*

/ouput/image

Dans output/images les fichiers de résultat de la compilation de buildroot : fichiers compressés image pour la raspberry

* tootfs.tar : tarball du système de fichier
* scard.img : le fichier à copier sur la sd scard


### Question 12 : *zimage* et *sdcard.img*

    file zImage
    zImage: Linux kernel ARM boot executable zImage (little-endian)

    file sdcard.img
    sdcard.img: DOS/MBR boot sector; partition 1 : ID=0xc, active, start-CHS (0x0,0,2), end-CHS (0x4,20,17), startsector 1, 65536 sectors; partition 2 : ID=0x83, start-CHS (0x4,20,18), end-CHS (0x1d,146,54), startsector 65537, 409600 sectors


### Question 13 : répertoire */tmp/rootfs*

C'est le système de fichier qui ira sur la Raspberry
(root file system)

priviliged oermet de desactiver certaine sécurité et autaurise le montage de répertoire de la machine hote dans le répertoire

chroot permet de changer de répertoire root

ON ARRIVE  à éxécuter l eprogramme car la simulation
transforme les ficheirs

peut émuler les instruction arm

## Partie 2: Flashage et UBoot

Tout d'abord, on récupère image de la carte SD dans le contener Docker.


Flashage de la carte SD :
 1. On trouve notre carte SD dans le répertoire */dev/* (`sudo fsdisk -l` :  liste tous les disques ou utilisation de `dmseg`).
 2. On supprime l'ensemble des partitions de la carde SD afin d'avoir une carte vierge (`sudo dd if=/dev/zero of=/dev/mmcblk0`).
 3. On copie l'image : `sudo dd if=sdcard.img of=/dev/sdx`, (status=progress) pour voir l'état. (
 if : input files, of : output files, dd : copie bit à bit, copier des images)

### Question 1 :

Il y a deux partitions :
* partition 1 : *overlays*
  partition avec le noyau, partition de boot
* partition 2: système de fichiers */bin/dev/etc*

### Question 2 : ports TX/RX

Port TX / RX port série : pin 8 et pin 10

Connexion  via le port série :
* via GTKterm
* baud rate dans le config text

cmdline : commande lancé au démarrage du kernel
cmdline : cat /proc/cmdline sur notre ordi

### Question 3 : Configuration du port série

Configuration du port série :
* baud rate 11520
(commande minicom `minicom -b 11520 -D /dev/tt..`)


### Question 4 : adresse IP

SSH réseau
Adresse ip :172.20.10.229

**Connexion en user :**
mot de passe : user1*
On le trouve dans *user.usertab* (`cat users.tables`)

**Connexion en root :**
mot de passe : root1*
On le trouve via `make menuconfig`
(dans le system configuration)

La connexion SSH en root ne fonctionne pas, le daemon ssh ne permet pas la connexion. Cela sécurise le Raspberry.
Pour configurer le ssh ==> aller dans le répertoire `/etc/ssh/ssh_config` et se mettre en super utilisateur


le kernel tout de suite on lance u-boot
http://www.delafond.org/traducmanfr/man/man5/ssh_config.5.html

modification dans le fichier /etc/ssh/sshd_config
répertoire /root ?

## U-BOOT

U-Boot est un bootloader permettant de charger différentes images.
Il faut donc configurer, compiler U-Boot dans Buildroot.

(aller dans le menu bootlooder de menuconfig)

### Question 6

* *u-boot.bin* : binaire du bootloader u-boot à mettre dans la partition overlays.le kernel tout de suite on lance u-boot.
* *boot.source* : configuration du bootloader que l'on peut ensuite compiler avec mkimage.
* modification du fichier *config.txt*

* u-boot fatload : load binary file from a dos filesystem
* u-boot setenv : set environment variables
* u-boot boot




## Partie 3 : GPIO et relais

Dans l'espace utilisateur, les GPIO sont accessible via le système de fichier */sys/class/GPIO*
(https://www.ics.com/blog/gpio-programming-using-sysfs-interface)






Partie 6 : BME280
Récupération des données capteurs via SPI e I2C

modprobe ==> chargement de module

### Question 2
sda : donnée
slc : clock

### Question 3
addressage des Port en hexadecimal 0x76


ground to ground 76

### Question 5
$

sudo ip link del docker0

espace kernel ??
le code kernel tourne et verifie les modifie les modification des fichiers

 * compile like this: cc bsd_userspace.c ../bme280.c -I ../ -o bme280

on peut modifier l'espace kernel : https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMFHS-087/Modification-des-appels-systemes-du-noyau-Linux-manipulation-de-la-memoire-du-noyau


typedef int8_t (*bme280_com_fptr_t)(uint8_t dev_id, uint8_t reg_addr, uint8_t *data, uint16_t len);
