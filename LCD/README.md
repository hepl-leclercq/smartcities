# LCD
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Le module `machine` de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe `I2C`, présente dans le module machine, est la classe utilisée pour la gestion de l'écran LCD. <BR>
Pour la partie LCD, l'affichage d'un message, l'affichage de la valeur d'un potentiomètre, et l'affichage de la température et de l'humidité sont présentés.
## Affichage d'un message

Code : [LCD_helloWorld](https://github.com/hepl-leclercq/smartcities/blob/8db6a8eeb2eee78df4381d38e745222d14f9b319/LCD/LCD_HelloWorld.py)

## Affichage valeur d'un potentiomètre

Code : [Led_BP_Interrupt]()

 
## Affichage de la température et de l'humidité

Code : [Led_BP_Interrupt](https://github.com/hepl-leclercq/smartcities/blob/0b574c7c24d3611e5b671a340976c71a10b51375/GPIO/Led_BP_Interrupt.py)


## La librairie LCD1602
La librairie LCD1602 est une bibliothèque de fonctions pour le Raspberry Pi Pico W qui permet de contrôler un écran LCD de type 1602. Cet écran LCD est doté de deux lignes de 16 caractères chacune.

Les fonctions de la librairie LCD1602 comprennent :

#### lcd_init() 
 Cette fonction initialise l'écran LCD en configurant les broches GPIO nécessaires. Cette fonction doit être appelée avant d'utiliser d'autres fonctions de la bibliothèque.

#### lcd_clear() 
Cette fonction efface tout le contenu de l'écran.

#### lcd_display_string() 
Cette fonction affiche une chaîne de caractères sur l'écran. Elle prend en entrée deux arguments : la chaîne de caractères à afficher et la position de départ sur l'écran.

#### lcd_display_char()
Cette fonction affiche un seul caractère à la position spécifiée sur l'écran.

#### lcd_set_cursor()
Cette fonction permet de définir la position du curseur sur l'écran.

#### lcd_scroll_left()
Cette fonction fait défiler le contenu de l'écran vers la gauche.

#### lcd_scroll_right()
Cette fonction fait défiler le contenu de l'écran vers la droite.

#### lcd_create_char()
Cette fonction permet de créer un caractère personnalisé à afficher sur l'écran. Elle prend en entrée un tableau de 8 octets représentant le motif du caractère.

#### lcd_blink()
Cette fonction permet de faire clignoter le curseur à la position actuelle.

#### lcd_no_blink()
Cette fonction arrête le clignotement du curseur.
 
## Les différentes fonctions
#### Fonction ``
 
#### Fonction ``
 
