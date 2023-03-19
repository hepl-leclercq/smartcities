# Importation de la classe LCD1602 depuis le fichier lcd1602.py
from lcd1602 import LCD1602

# Importation des classes I2C, Pin, ADC, PWM depuis le module machine
# Importation de la fonction sleep depuis le module utime
from machine import I2C, Pin, ADC, PWM
from utime import sleep

# Initialisation d'un objet ADC pour lire la valeur du capteur de position angulaire
ROTARY_ANGLE_SENSOR = ADC(0)

# Initialisation d'un objet I2C pour communiquer avec l'écran LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Initialisation d'un objet LCD1602 avec les paramètres suivants :
# - i2c : l'objet I2C pour communiquer avec l'écran - 2 : le nombre de lignes de l'écran - 16 : le nombre de caractères par ligne
d = LCD1602(i2c, 2, 16)

# Affichage des caractères de démarrage sur l'écran
d.display()

# Boucle infinie
while True:
    # Attente d'une seconde
    sleep(1)
    # Effacement de l'écran
    d.clear()
    # Positionnement du curseur en haut à gauche de l'écran
    d.setCursor(0, 0)
    # Affichage de la valeur lue sur le capteur de position angulaire, convertie en chaîne de caractères
    d.print(str(ROTARY_ANGLE_SENSOR.read_u16()))
    # Attente d'une seconde
    sleep(1)
