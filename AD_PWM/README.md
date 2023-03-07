# AD - PWM
## Introduction
Dans le cadre du cours de Smartcities, il nous est demandé de réaliser plusieurs applications autour du Raspberry Pi Pico W, en utilisant le shield Grove founit avec.
Le module "machine" de Raspberry Pi Pico est une bibliothèque Python qui fournit une interface pour accéder aux fonctionnalités matérielles de la carte, telles que les GPIO, les interfaces SPI, I2C, UART, ADC, DAC, PWM, entre autres. Il permet de contrôler et d'interagir avec ces périphériques en utilisant des instructions Python simples, facilitant ainsi la programmation de projets embarqués. 
Pour la partie PWM, la lecture d'un potentiomètre et l'utilisation d'un signal PWM pour la génération d'une musique sont présentés.
## Lecture du potentiomètre
Utilisation de l'objet ADC pour la lecture de la valeur d'un potentiomètre, et conversion de cette valeur en un angle compris entre 30 et 330 degrés. <BR>
Code : [Pot_angle](https://github.com/hepl-leclercq/smartcities/blob/52242becf5d6158fb5e8ecf648cea9acf3f825bd/AD_PWM/Pot_angle.py)

## Signal PWM en fonction de la valeur du potentiomètre
  Utilisation de l'objet ADC et PWM du module machine pour lire la valeur d'un potentiomètre, et generer un signal PWM de même valeur, pour dimmer l'allumage d'une LED.

## Création d'une musique
