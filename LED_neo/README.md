Le module `neopixel` est une bibliothèque en MicroPython pour contrôler des bandes de LEDs RGB de type Neopixel. Il s'agit d'un module très pratique pour créer des effets lumineux.

Les fonctions principales du module neopixel sont les suivantes :

`neopixel.NeoPixel(pin, n, bpp=3, timing=1)` : cette fonction crée une instance de la classe neopixel.NeoPixel.

`NeoPixel.__setitem__(self, index, val)` : cette méthode permet de définir la couleur d'un pixel à l'indice index. 

`NeoPixel.write()` : cette méthode envoie les données des pixels à la bande de LED. Elle doit être appelée chaque fois que les couleurs des pixels ont été modifiées.

`NeoPixel.fill(self, color)` : cette méthode remplit tous les pixels de la bande avec la couleur spécifiée par color.

`NeoPixel.clear(self)` : cette méthode éteint tous les pixels de la bande.


