# Importation des bibliothèques nécessaires
from machine import Pin, PWM
import utime

# Initialisation de la PWM sur la broche 18 avec une fréquence de 500 Hz
pwm = PWM(Pin(18))
pwm.freq(500)

# Boucle infinie
while True:
    # Boucle sur les valeurs de 0 à 19
    for i in range(20):
        # Variation linéaire de la luminosité en fonction de i
        pwm.duty_u16(i*3276)

        # Variation quadratique de la luminosité en fonction de i
        pwm.duty_u16(i*i*128)

        # Pause de 100 millisecondes avant de passer à la valeur suivante
        utime.sleep_ms(100)
