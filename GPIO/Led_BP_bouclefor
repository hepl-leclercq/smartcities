import machine  # import de la librairie machine pour accéder aux pins
import utime # import de la librairie utime pour gérer les délais

LED = machine.Pin (16,machine.Pin.OUT) # définition de la pin 16 en sortie pour la LED
Button = machine.Pin (18, machine.Pin.IN) # définition de la pin 18 en entrée pour le bouton poussoir


while True: # boucle infinie
    if Button.value() == 1: # si le bouton poussoir est pressé
        for i in range(10): # boucle for allant de 0 à 9
            LED.value(1) # allume la LED
            utime.sleep_ms(200) # attend 200 millisecondes
            LED.value(0) # éteint la LED
            utime.sleep_ms(200) # attend 200 millisecondes
            
