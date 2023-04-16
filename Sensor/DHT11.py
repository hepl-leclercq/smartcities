# Importe la classe DHT11 depuis le module dht
from dht import DHT11

# Importe la classe Pin depuis le module machine, ainsi que la fonction I2C et la fonction sleep depuis le module utime
from machine import Pin, I2C
from utime import sleep

# Crée une instance du capteur DHT11 en utilisant la broche 18
dht11 = DHT11(Pin(18))

# Boucle infinie
while True:
    # Attend 2 secondes avant de continuer
    sleep(2)
    # Déclenche une mesure de température et d'humidité avec le capteur DHT11
    dht11.measure()
    # Affiche la température mesurée
    print(dht11.temperature())
    # Affiche l'humidité mesurée
    print(dht11.humidity())
