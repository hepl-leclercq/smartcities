# Sensor

## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Pour la partie Network, plusieurs librairies sont utilisées et expliquées, tel que `network`, `urequests` et `ntptime`.

Pour la partie SENSOR, l'affichage de la température et humidité, l'affichage de la valeur d'un microphone et de luminosité entre 0 et 65535, et la détection de mouvement via un capteur PIR sont présentés. 
  
## Affichage de température et humidité
Utilisation de la fonction `dht11.measure()`, `dht11.temperature()` et `dht11.humidity()` pour afficher la température et l'humidité dans le moniteur série.
Code : [DHT11](https://github.com/hepl-leclercq/smartcities/blob/25dd11630cc4ba6d2fc0b74e16389c21efe1a084/Sensor/DHT11.py)

## Affichage valeur d'un microphone entre 0 et 65535
Utilisation de la fonction `read_u16()` de la classe ADC pour réaliser la conversion du signal analogique provenant du microphone, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, affichage de cette valeur dans le moniteur série.<BR>
Code : [Microphone](https://github.com/hepl-leclercq/smartcities/blob/d682f84a1e919442229988c2709c72d33f14307a/Sensor/Microphone.py)


## Affichage valeur de luminosité entre 0 et 65535
Utilisation de la fonction `read_u16()` de la classe ADC pour réaliser la conversion du signal analogique provenant du capteur de luminosité, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, affichage de cette valeur dans le moniteur série.<BR>
Code : [Luminosité](https://github.com/hepl-leclercq/smartcities/blob/1d4312304688b8958dbeec5996d4708257e0106e/Sensor/Microphone.py)

## Affichage d'un message lorsque un obstacle est détecté
Utilisation des fonctions du GPIO pour détecter un osctacle, et affichage d'un message dans le moniteur série.
Les capteurs PIR sont des capteurs utilisés pour détecter les mouvements. Ils détectent les changements de température dans leur champ de vision.<BR>
Code : [PIR](https://github.com/hepl-leclercq/smartcities/blob/86b89f94d8a6c2390578bca4f81dcb9ef8a69d90/Sensor/PIR.py)


## Module `dht`
Le module `dht` en Micropython est une bibliothèque qui permet de lire les données de température et d'humidité à partir du capteur DHT11 ou DHT22. Voici quelques-unes de ses fonctions principales :

`dht.DHT11(pin)` : Crée une instance du capteur DHT11 en utilisant le numéro de broche spécifié. 

`d.measure()` : Déclenche une mesure de température et d'humidité. Cette fonction doit être appelée avant de lire les données.

`d.temperature()` : Renvoie la température en degrés Celsius sous forme de nombre à virgule flottante.

`d.humidity()` : Renvoie l'humidité relative en pourcentage sous forme de nombre à virgule flottante. 

Il convient de noter que la fonction d.measure() peut prendre un certain temps pour effectuer la mesure, et il est recommandé d'attendre au moins 2 secondes entre les mesures successives pour éviter de surcharger le capteur.
