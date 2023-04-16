# Importe le module machine
import machine

# Crée une instance du port ADC en utilisant l'entrée ADC 1
luminosite_adc = machine.ADC(0)

# Boucle infinie
while True:
    # Lecture de la valeur analogique sur le port ADC
    lum = luminosite_adc.read_u16()

    # Affichage de la valeur lue
    print(lum)
