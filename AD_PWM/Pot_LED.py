from machine import Pin, ADC, PWM   # Importe les classes Pin, ADC et PWM depuis le module machine

ROTARY_ANGLE_SENSOR = ADC(0)   # Crée un objet ADC pour lire la valeur du capteur rotatif
LED_PWM = PWM(Pin(18))   # Crée un objet PWM pour contrôler la LED connectée à la broche 18

LED_PWM.freq(500)   # Configure la fréquence du signal PWM à 500 Hz

while True:   # Boucle infinie
    val = ROTARY_ANGLE_SENSOR.read_u16()   # Lit la valeur du capteur rotatif
    LED_PWM.duty_u16(val)   # Configure le rapport cyclique du signal PWM en fonction de la valeur lue du capteur rotatif
