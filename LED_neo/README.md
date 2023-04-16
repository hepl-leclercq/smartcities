# LED_NEO

## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Le module `machine` de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. <BR> On fournit également au Raspberry Pi Pico W la librairie `ws2812`, elle permet de faciliter l'utilisation des leds néopixels. Cette librairie est expliquée en bas de page.
Pour la partie LED_NEO, la gestion d'une led RGB, allumée par des couleurs différentes, est présenté. 

## Différentes couleurs sur la LED néopixel
Utilisation des fonction `pixels_fill()` et `pixels_show()` pour allumer une led en différentes couleurs. <BR>
Code : [LedColor](https://github.com/hepl-leclercq/smartcities/blob/171dfe7ae4de1d1d756b8420d6eb51be53f82a9f/LED_neo/LedColor.py)

## Le module `ws2812`

Le module `ws2812` est une bibliothèque en MicroPython pour contrôler des bandes de LEDs RGB de type Neopixel. Il s'agit d'un module très pratique pour créer des effets lumineux.


Les fonctions principales du module ws2812 sont les suivantes :

`pixels_show():` : cette méthode envoie les données des pixels à la bande de LED. Elle doit être appelée chaque fois que les couleurs des pixels ont été modifiées.

`pixels_fill()` : cette méthode remplit tous les pixels de la bande avec la couleur spécifiée par color.





