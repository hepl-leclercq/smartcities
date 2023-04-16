from ws2812 import WS2812  # importe la bibliothèque pour contrôler les LED WS2812
import utime  # importe la bibliothèque de gestion du temps pour les pauses

# définit des couleurs prédéfinies pour les LED WS2812
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

# initialise la broche de données de la LED WS2812 et le nombre de LED
led = WS2812(18, 1)  # WS2812(pin_num,led_count)

# boucle infinie pour changer la couleur de la LED WS2812
while True:
    print("fills")  # affiche un message de débogage
    for color in COLORS:  # itère à travers chaque couleur prédéfinie
        led.pixels_fill(color)  # change la couleur de toutes les LED
        led.pixels_show()  # affiche la couleur sur toutes les LED
        utime.sleep(0.2)  # fait une pause de 0,2 seconde pour observer la couleur avant de passer à la suivante
