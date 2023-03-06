# GPIO
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.
Le module "machine" de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. 
Pour la partie GPIO, la gestion d'une Led, d'un bouton et d'une interruption via un bouton sont requises.
## Led et bouton
Utilisation des méthodes "for" et "while", ainsi que un bouton poussoir, pour le contrôle d'une LED. <br> 
**Appuie bouton poussoir** : Led clignote 10x.<br>
Code : [Led_BP_bouclefor](https://github.com/hepl-leclercq/smartcities/blob/4bdb1034d0ef0033ecef4018052e9c295b761aa2/GPIO/Led_BP_bouclefor.py)

## Interruption
Utilisation de l'interruption sur le bouton poussoir pour gérer le temps de clignotement d'une Led : <br> 
**Pas d'appuie** : Led allumée. <br>
**Appuie x fois** : Led clignotte à intervalle (1/x) secondes.<br>
**x = 15** : Reset le programme<br>
Code : [Led_BP_Interrupt](https://github.com/hepl-leclercq/smartcities/blob/0b574c7c24d3611e5b671a340976c71a10b51375/GPIO/Led_BP_Interrupt.py)
