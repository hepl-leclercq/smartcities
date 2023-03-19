# Importation des classes LCD1602 et DHT11 depuis les fichiers lcd1602.py et dht.py
from lcd1602 import LCD1602
from dht import DHT11

# Importation des classes I2C, Pin, ADC, PWM depuis le module machine
# Importation de la fonction sleep depuis le module utime
from machine import I2C, Pin, ADC, PWM
from utime import sleep

# Initialisation d'un objet DHT11 avec la pin 18 du microcontrôleur pour lire la température et l'humidité de l'air
dht11 = DHT11(Pin(18))

# Initialisation d'un objet I2C pour communiquer avec l'écran LCD
i2c_1 = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Initialisation d'un objet LCD1602 avec les paramètres suivants :
# - i2c_1 : l'objet I2C pour communiquer avec l'écran - 2 : le nombre de lignes de l'écran - 16 : le nombre de caractères par ligne
d = LCD1602(i2c_1, 2, 16)

# Affichage des caractères de démarrage sur l'écran
d.display()

# Effacement de l'écran
d.clear()

# Boucle infinie
while True:
    # Attente de 1 seconde
    sleep(1)
    # Mesure de la température et de l'humidité de l'air avec le capteur DHT11
    dht11.measure()
    # Effacement de l'écran
    d.clear()
    # Positionnement du curseur en haut à gauche de l'écran
    d.setCursor(0, 0)
    # Affichage de la température lue sur le capteur, convertie en chaîne de caractères
    d.print(str(dht11.temperature()))
    # Écriture du symbole °C sur l'écran à côté de la température
    d.write(0b11011111)
