# Importe les modules Pin et sleep du module machine
from machine import Pin
from time import sleep

# Définit les broches de détection de mouvement et de la LED
motion_pin = Pin(20, Pin.IN)
led_pin = Pin(25, Pin.OUT)

# Définit les constantes de temps
ON_TIME = 5       
SLEEP_TIME = 0.5
countdown = 0

# Boucle infinie
while True:
    # Si un mouvement est détecté
    if motion_pin.value():
        # Affiche un message
        print("obstacle détecté")

   
