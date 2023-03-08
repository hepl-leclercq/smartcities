# GPIO
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.<BR>
Le module `machine` de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe `PIN`, présente dans le module machine, est la classe utilisée pour la gestion des GPIO. Elle permet de configurer et de contrôler les broches d'E/S de la carte. Donc de configurer la direction d'une broche comme entrée ou sortie, de lire ou d'écrire la valeur d'une broche, et de configurer des interruptions pour les changements d'état d'une broche. 
Pour la partie GPIO, la gestion d'une Led, d'un bouton et d'une interruption via un bouton sont présentés.
## Led et bouton
Utilisation des méthodes `for` et `while`, ainsi que un bouton poussoir, pour le contrôle d'une LED. La fonction `value()` est utilisée pour lire l'état de mon bouton poussoir, et aussi pour écrire l'état de ma LED. <br> 
**Appuie bouton poussoir** : Led clignote 10x.<br>
Code : [Led_BP_bouclefor](https://github.com/hepl-leclercq/smartcities/blob/4bdb1034d0ef0033ecef4018052e9c295b761aa2/GPIO/Led_BP_bouclefor.py)

## Interruption
Utilisation de l'interruption sur le bouton poussoir pour gérer le temps de clignotement d'une Led. La fonction `IRQ()` permet de configurer l'interruption sur la broche du bouton poussoir, et de définir la fonction appelée `interrupt()`. La fonction `interrupt()` appelle la fonction `update_value()`, qui va incrémenter de 1 la variable val. Cette variable définit la vitesse de clignotement, tel que : <br> 
**Pas d'appuie** : Led allumée. <br>
**Appuie 'val' fois** : Led clignotte à intervalle (1/(1+val)) secondes.<br>
**'val' = 15** : Reset le programme<br>
Code : [Led_BP_Interrupt](https://github.com/hepl-leclercq/smartcities/blob/0b574c7c24d3611e5b671a340976c71a10b51375/GPIO/Led_BP_Interrupt.py)

## Les différentes fonctions
#### Fonction `value()`
La fonction value() peut être utilisée avec deux modes de fonctionnement différents : le mode lecture et le mode écriture.<BR> **En mode lecture**, `value()` est utilisée pour lire la valeur actuelle du pin d'E/S. Cette fonction renvoie un booléen de valeur 1 lorsque l'entrée est à l'état logique haut, et un booléen de valeur 0 lorsque l'entrée est à l'état logique bas. <BR> **En mode écriture**, `value()` est utilisée pour écrire une nouvelle valeur sur le pin d'E/S, tel que `sortie.value(1)` met la sortie à l'état logique 1, et `sortie.value(0)` met la sortie à l'état logique 0.
 
#### Fonction `IRQ()`
La fonction `IRQ()` est utilisée pour activer ou désactiver l'interruption d'événement sur une broche GPIO spécifique. <BR>
Cette fonction prend un ou plusieurs arguments pour configurer l'interruption, qui sont les suivants :

- `trigger`: le type de déclencheur d'interruption à utiliser, qui peut être l'un des suivants :
  - `Pin.IRQ_RISING`: déclenche l'interruption lorsqu'il y a une transition de bas à haut de la broche.
  - `Pin.IRQ_FALLING`: déclenche l'interruption lorsqu'il y a une transition de haut à bas de la broche.
  - `Pin.IRQ_RISING_FALLING`: déclenche l'interruption lorsqu'il y a une transition de bas à haut ou de haut à bas de la broche.
- `handler`: la fonction à appeler lorsque l'interruption est déclenchée.
- `debounce`: le temps de rebond (en millisecondes) à appliquer à la broche pour éviter les rebonds de signal. La valeur par défaut est 0, ce qui signifie qu'aucun temps de rebond n'est appliqué.
  
