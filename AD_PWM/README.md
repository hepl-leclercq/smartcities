# AD - PWM
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.
Le module "machine" de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. La classe `ADC` (Analog-to-Digital Converter) présente dans le module machine, est une classe qui permet d'effectuer des conversions analogiques-numériques sur les broches d'entrée analogiques de la carte.
Pour la partie PWM, la lecture d'un potentiomètre, l'utilisation d'un signal PWM pour le dimming linéaire et quadratique, et la génération d'une musique sont présentés.
## Lecture du potentiomètre
La fonction `read()` de la classe `ADC` est utilsée pour réaliser la conversion du signal analogique provenant du potentiomètre, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. Ensuite, conversion de cette valeur en un angle compris entre 30 et 330 degrés.   <BR>
Code : [Pot_angle](https://github.com/hepl-leclercq/smartcities/blob/52242becf5d6158fb5e8ecf648cea9acf3f825bd/AD_PWM/Pot_angle.py)

## Signal PWM en fonction de la valeur du potentiomètre
La fonction `read()` de la classe `ADC` est utilsée pour réaliser la conversion du signal analogique provenant du potentiomètre, en une valeur binaire 12 bits, donc comprise entre 0 et 65535. La fonction `duty()` de la classe `ADC` permet ensuite de générer un signal PWM dont le rapport cyclique est définit par la valeur accquise par la fonction `read()` précédente. Ce signal PWM permet de dimmer l'intensité lumineuse de la LED. <BR>
Code : [Pot_LED](https://github.com/hepl-leclercq/smartcities/blob/fae5f5ee30da61839b5e29f9089763c6f4e1b1fb/AD_PWM/Pot_LED.py)
## Dimming d'une Led de façon linéaire et quadratique
  Utilisation de la fonction `duty()` pour définir le rapport cyclique de la PWM. Cette PWM dimme l'intensité lumineuse de la LED. Ce programme contient 2 méthodes pour la variation de luminosité : la méthode linéaire et la méthode quadratique.
Code : [Lin&Quad_dimmingLed](https://github.com/hepl-leclercq/smartcities/blob/0a0aa7913e14d9f004b816ff375e80577415b072/AD_PWM/Lin&Quad_dimmingLed.py)
## Création d'une musique
Utilisation de la PWM sur le Buzzer pour la création d'une musique. La largeur d'impulsion de la PWM agit sur le volume et est définit par la fonction `duty()`. La fréquence de la PWM agit sur la fréquence de la note et est définit par la fonction `freq()`. Le morceau généré est "Final Countdown" de "Europe".<BR>
Code = [Final_Countdown_Buzzer](https://github.com/hepl-leclercq/smartcities/blob/4b91a1f2deeb30321c6f24695a13a5e49e7f2d20/AD_PWM/Final_Countdown_Buzzer.py)

  
