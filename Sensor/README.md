## Sensor

# LCD
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Le module `machine` de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe `I2C`, présente dans le module machine, est la classe utilisée pour la gestion de l'écran LCD. <BR> On fournit également au Raspberry Pi Pico W la librairie `DHT11`, elle permet de faciliter l'utilisation du capteur DHT11. Cette librairie est expliquée en bas de page.
Pour la partie SENSOR, l'affichage de la température et humidité, l'affichage de la valeur d'un microphone et de luminosité entre 0 et 65535, et la détection de mouvement via un capteur PIR sont présentés. 
  
## Affichage de température et humidité
Utilisation de la fonction `dht11.measure()`, `dht11.temperature()` et `dht11.humidity()` pour afficher la température et l'humidité dans le moniteur série.
Code : [DHT11](https://github.com/hepl-leclercq/smartcities/blob/25dd11630cc4ba6d2fc0b74e16389c21efe1a084/Sensor/DHT11.py)

## Affichage valeur d'un microphone entre 0 et 65535
Utilisation de la fonction `read_u16()` de la classe ADC pour réaliser la conversion du signal analogique provenant du microphone, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, affichage de cette valeur dans le moniteur série.
Code : [Microphone](https://github.com/hepl-leclercq/smartcities/blob/d682f84a1e919442229988c2709c72d33f14307a/Sensor/Microphone.py)


## Affichage valeur de luminosité entre 0 et 65535
Utilisation de la fonction `read_u16()` de la classe ADC pour réaliser la conversion du signal analogique provenant du capteur de luminosité, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, affichage de cette valeur dans le moniteur série.
Code : [Luminosité](https://github.com/hepl-leclercq/smartcities/blob/e0ef1af58e0330a146b9543ac2ed2f8200d50196/Sensor/Luminosite.py)

## Affichage d'un message lorsque un obstacle est détecté
Utilisation des fonctions du GPIO pour détecter un osctacle, et affichage d'un message dans le moniteur série.
Code : [PIR](https://github.com/hepl-leclercq/smartcities/blob/0a1bee5396817405c3152025b54c753057f48a88/Sensor/PIR.py)



Le module `dht` en Micropython est une bibliothèque qui permet de lire les données de température et d'humidité à partir du capteur DHT11 ou DHT22. Voici quelques-unes de ses fonctions principales :

`dht.DHT11(pin)` : Crée une instance du capteur DHT11 en utilisant le numéro de broche spécifié. 

`d.measure()` : Déclenche une mesure de température et d'humidité. Cette fonction doit être appelée avant de lire les données.

`d.temperature()` : Renvoie la température en degrés Celsius sous forme de nombre à virgule flottante.

`d.humidity()` : Renvoie l'humidité relative en pourcentage sous forme de nombre à virgule flottante. 

Il convient de noter que la fonction d.measure() peut prendre un certain temps pour effectuer la mesure, et il est recommandé d'attendre au moins 2 secondes entre les mesures successives pour éviter de surcharger le capteur.

Code : (code) <https://github.com/hepl-leclercq/smartcities/blob/25dd11630cc4ba6d2fc0b74e16389c21efe1a084/Sensor/DHT11.py>

### Microphone
Le microphone se branche sur une broche GPIO du Raspberry Pi Pico pour fournir une entrée audio analogique.

Une fois connecté, il est possible de lire les données audio à l'aide d'un script MicroPython. Le module machine peut être utilisé pour configurer le port GPIO connecté au microphone en tant que canal ADC et pour lire les données audio.

Il est également possible d'utiliser des bibliothèques tierces telles que PyAudio pour traiter les données audio lues à partir du microphone et effectuer des tâches telles que la reconnaissance vocale ou la détection de motifs sonores.

Notre code microphone nous utilisons le microphone comme un simple object ADC et donc on ne peut lire que la tension et l'afficher de 0 à 65535.

Luminosité
Ce capteur renvoit simplement une tension qui défini la luminosité. Nous allons donc le virtualisé en un object ADC ensuite lire la valeur en 16 bits. Cette valeur peut être utilisé pour définir des conditions et des régles en fonction de la lumière.

PIR (Passive Infrared Sensor)
Les capteurs PIR sont des capteurs utilisés pour détecter les mouvements. Ils détectent les changements de température dans leur champ de vision, ce qui leur permet de détecter les mouvements des personnes ou des animaux.

Le fonctionnement des capteurs PIR est basé sur le principe de la détection infrarouge passive. Ils sont composés d'un pyroélément qui convertit les variations de température en signaux électriques. Lorsqu'une personne ou un animal se déplace dans le champ de vision du capteur, il émet une quantité de chaleur différente de celle de l'environnement, ce qui déclenche une variation de température et un signal électrique est produit par le pyroélément.

Ce code utilise un capteur PIR connecté à la broche 20 pour détecter des mouvements. Lorsqu'un mouvement est détecté, la LED connectée à la broche 25 s'allume pendant 10 secondes. Ensuite, la LED s'éteint et le code retourne en attente de détection de mouvements.
