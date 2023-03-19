# LCD
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Le module `machine` de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe `I2C`, présente dans le module machine, est la classe utilisée pour la gestion de l'écran LCD. <BR> On fournit également au Raspberry Pi Pico W la librairie `LCD1602`, elle permet de faciliter l'utilisation de l'écran LCD. Ses fonctions principales sont expliquées en bas de page.<BR>
Pour la partie LCD, l'affichage d'un message, l'affichage de la valeur d'un potentiomètre, et l'affichage de la température et de l'humidité sont présentés.
## Affichage d'un message
Utilisation de la fonction `setCursor()` et `print()` pour afficher un message sur l'écran LCD.<br>
Code : [LCD_helloWorld](https://github.com/hepl-leclercq/smartcities/blob/8db6a8eeb2eee78df4381d38e745222d14f9b319/LCD/LCD_HelloWorld.py)

## Affichage valeur d'un potentiomètre
Utilisation de la fonction `read_u16()` de la classe ADC  pour réaliser la conversion du signal analogique provenant du potentiomètre, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, affichage de cette valeur sur l'écran LCD, avec la fonction `print()`.<br>
Code : [LCD_potval](https://github.com/hepl-leclercq/smartcities/blob/a9b008b12753e93c37d20290306a38a49b14f791/LCD/LCD_potval.py)

 
## Affichage de la température
Récuperation chaque seconde de la température via la pin D18 du Raspberry Pi Pico W connectée au capteur de température, et affichage de cette température sur l'écran LCD, en ajoutant le logo `°`.<br>
Code : [LCD_temp](https://github.com/hepl-leclercq/smartcities/blob/9b523c6d9dde85a7f951ad25c7986eba10be9ad7/LCD/LCD_temp.py)


## La librairie LCD1602
La librairie LCD1602 est une bibliothèque de fonctions pour le Raspberry Pi Pico W qui permet de contrôler un écran LCD de type 1602. Cet écran LCD est doté de deux lignes de 16 caractères chacune.

Les fonctions de la librairie LCD1602 comprennent :

#### lcd_init() 
Cette fonction initialise l'écran LCD en configurant les broches GPIO nécessaires. Cette fonction doit être appelée avant d'utiliser d'autres fonctions de la bibliothèque.

#### lcd_clear() 
Cette fonction efface tout le contenu de l'écran.

#### lcd_setCursor(x, y)
Cette fonction déplace le curseur à la position (x,y), où x et y sont des entiers compris entre 0 et 15 pour les écrans LCD de 16x2.

#### lcd_no_display() 
Cette fonction éteint l'affichage.

#### lcd_display() 
Cette fonction allume l'affichage.

#### lcd_no_cursor() 
Cette fonction masque le curseur.

#### lcd_cursor()
Cette fonction affiche le curseur sous forme de trait clignotant.

#### lcd_create_char()
Cette fonction permet de créer un caractère personnalisé à afficher sur l'écran. Elle prend en entrée un tableau de 8 octets représentant le motif du caractère.

#### lcd_blink()
Cette fonction permet de faire clignoter le curseur à la position actuelle.

#### lcd_no_blink()
Cette fonction arrête le clignotement du curseur.

#### lcd_autoscroll()
Cette fonction fait défiler automatiquement le texte vers la gauche lorsque le curseur atteint le bord droit de l'écran

#### lcd_no_autoscroll()
Cette fonction désactive le défilement automatique.

#### print(value)
Cette fonction affiche une chaîne de caractères sur l'écran LCD à la position actuelle du curseur.

 
