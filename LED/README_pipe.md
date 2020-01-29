# Test sur sa propre machine:
## Code python:

Exécuter dans un terminal:

* `$ python pipe.py`

## Code:

Pour compiler dans un autre terminal:
* `$ gcc -o pipe_exec pipe.c`

Puis lancer le fichier executable:
* `$ ./pipe_exec`

# Test sur raspberry:
## Code python:

Il faut faire le cablage des LED au préalable.
Rien à compiler mais le fichier python à tester est le GPIO.py:

* `$ python GPIO.py`

## Code C:

Il faut ajouter la partie ouverture de pipe et écriture dans le pipe puis le fermer après écriture de l'état voulu.
Puis cross-compiler sur la raspberry.

# Branchement:

Les LED possèdent une borne - (branche la plus courte), et une borne + (branche la plus grande).
Il faut brancher les bornes - des LED sur une ligne reliée à la masse de la raspberry ou du port série qui sert à la transmission de données avec la raspberry.
Ensuite la borne + de la LED rouge doit être branchée au GPIO 17 donc au port n°11, la LED verte elle doit être branchée au GPIO 27 juste à côté donc au port n°13.
