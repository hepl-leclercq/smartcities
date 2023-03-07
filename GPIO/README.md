# GPIO
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.
Le module 'machine' de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe 'PIN', présente dans le module machine, est la classe utilisée pour la gestion des GPIO. Elle permet de configurer et de contrôler les broches d'E/S de la carte. Donc de configurer la direction d'une broche comme entrée ou sortie, de lire ou d'écrire la valeur d'une broche, et de configurer des interruptions pour les changements d'état d'une broche. 
Pour la partie GPIO, la gestion d'une Led, d'un bouton et d'une interruption via un bouton sont présentés.
## Led et bouton
Utilisation des méthodes 'for' et 'while', ainsi que un bouton poussoir, pour le contrôle d'une LED. La fonction 'value()' est utilisée pour lire l'état de mon bouton poussoir, et aussi pour écrire l'état de ma LED. <br> 
**Appuie bouton poussoir** : Led clignote 10x.<br>
Code : [Led_BP_bouclefor](https://github.com/hepl-leclercq/smartcities/blob/4bdb1034d0ef0033ecef4018052e9c295b761aa2/GPIO/Led_BP_bouclefor.py)

## Interruption
Utilisation de l'interruption sur le bouton poussoir pour gérer le temps de clignotement d'une Led. La fonction 'IRQ()' permet de configurer l'interruption sur la broche du bouton poussoir, et de définir la fonction appelée 'interrupt()'. La fonction 'interrupt()' appelle la fonction 'update_value()', qui va incrémenter de 1 la variable val. Cette variable définit la vitesse de clignotement, tel que : <br> 
**Pas d'appuie** : Led allumée. <br>
**Appuie 'val' fois** : Led clignotte à intervalle (1/(1+val)) secondes.<br>
**'val' = 15** : Reset le programme<br>
Code : [Led_BP_Interrupt](https://github.com/hepl-leclercq/smartcities/blob/0b574c7c24d3611e5b671a340976c71a10b51375/GPIO/Led_BP_Interrupt.py)
