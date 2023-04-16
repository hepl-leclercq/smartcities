# Importe le module machine
import machine
import time

# Crée une instance du port ADC
mic = machine.ADC(0)

# Boucle infinie
while True:
    # Lecture de la valeur analogique
    audio_level = mic.read_u16()
    # Affiche la valeur lue
    print(audio_level)
    # Attend 0,1 seconde avant de continuer
    time.sleep(0.1)
