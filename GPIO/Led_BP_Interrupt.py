from machine import Pin  # import de la classe Pin depuis le module machine
import utime # import du module utime
val = 0 # initialisation de la variable val à 0
time = 0 # initialisation de la variable time à 0
LED = Pin (16,machine.Pin.OUT) # création d'une instance de la classe Pin pour la LED sur le GPIO 16
Button = Pin (18, machine.Pin.IN) # création d'une instance de la classe Pin pour le bouton poussoir sur le GPIO 18

def interrupt(p): # définition de la fonction interrupt pour gérer l'interruption sur le bouton poussoir
    update_value() # appel de la fonction update_value()
    
def update_value():  # définition de la fonction update_value pour mettre à jour les variables val et time
        global val, time # utilisation de la directive global pour accéder aux variables globales val et time
        val = val + 1  # incrémentation de la variable val
        time = 1000 / val # calcul de la variable time en fonction de la valeur de val
        
        

Button.irq(interrupt,trigger=Pin.IRQ_RISING) # configuration de l'interruption sur le bouton poussoir
    
while True : # boucle principale infinie du programme
    
    if (val == 0): # si la valeur de val est égale à 0
        LED.value(1)  # allumage de la LED
    elif (val != 0): # sinon, si la valeur de val est différente de 
        LED.value(1)  # allumage de la LED
        utime.sleep_ms(int(time)) # attente d'un temps équivalent à la valeur de time
        LED.value(0) # extinction de la LED
        utime.sleep_ms(int(time)) # attente d'un temps équivalent à la valeur de time
        if val == 15: # si la valeur de val est égale à 15
            val = 0 # réinitialisation de la variable val à 0 et reset du programme
