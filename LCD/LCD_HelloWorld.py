# Importation des modules nécessaires
from lcd1602 import LCD1602
from machine import I2C, Pin
from utime import sleep

# Initialisation de la communication I2C avec l'écran LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# Initialisation de l'objet LCD1602 avec les paramètres 2 et 16 pour un écran 2x16
d = LCD1602(i2c, 2, 16)

# Allumage de l'écran
d.display()

# Attente d'une seconde
sleep(1)

# Effacement de l'écran
d.clear()

# Affichage du texte "Hello"
d.print('Hello')

# Attente d'une seconde
sleep(1)

# Positionnement du curseur à la première colonne de la deuxième ligne
d.setCursor(0, 1)

# Affichage du texte "World" sur la deuxième ligne
d.print('World')
