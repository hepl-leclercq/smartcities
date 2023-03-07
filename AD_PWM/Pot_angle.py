from machine import ADC    # Importe la classe ADC depuis le module machine
from utime import sleep    # Importe la fonction sleep depuis le module utime

ROTARY_ANGLE_SENSOR = ADC(0)    # Crée un objet ADC pour lire la valeur du capteur rotatif

while True:    # Boucle infinie
    lecture_capteur = ROTARY_ANGLE_SENSOR.read_u16()    # Lit la valeur du capteur rotatif
    print(lecture_capteur)    # Affiche la valeur lue du capteur rotatif
    angle_degrees = (lecture_capteur - 0) * (330 - 30) / (65535 - 0) + 30    # Calcule l'angle en degrés à partir de la valeur lue
    print("angle = ", end='')    # Affiche le texte "angle = " sans saut de ligne
    print(angle_degrees)    # Affiche l'angle en degrés calculé
    sleep(1)    # Attend une seconde avant de lire à nouveau la valeur du capteur rotatif 
