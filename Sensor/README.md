## Sensor
### DHT11
Le capteur DHT11 est un capteur de température et d'humidité relativement simple et peu coûteux. Il utilise un capteur capacitif pour mesurer l'humidité relative et un thermistor pour mesurer la température ambiante. Les données sont généralement transmises sous forme numérique via un seul fil, ce qui le rend facile à intégrer dans des projets électroniques.


Le module `dht` en Micropython est une bibliothèque qui permet de lire les données de température et d'humidité à partir du capteur DHT11 ou DHT22. Voici quelques-unes de ses fonctions principales :

`dht.DHT11(pin)` : Crée une instance du capteur DHT11 en utilisant le numéro de broche spécifié. 

`d.measure()` : Déclenche une mesure de température et d'humidité. Cette fonction doit être appelée avant de lire les données.

`d.temperature()` : Renvoie la température en degrés Celsius sous forme de nombre à virgule flottante.

`d.humidity()` : Renvoie l'humidité relative en pourcentage sous forme de nombre à virgule flottante. 

Il convient de noter que la fonction d.measure() peut prendre un certain temps pour effectuer la mesure, et il est recommandé d'attendre au moins 2 secondes entre les mesures successives pour éviter de surcharger le capteur.

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
