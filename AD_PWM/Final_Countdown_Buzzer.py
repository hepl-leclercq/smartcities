from machine import Pin, I2C, ADC, PWM # Importation de différentes classes depuis le module machine
from time import sleep # Importation de la fonction sleep depuis le module time

buzzer = PWM(Pin(27)) # Initialisation d'un objet PWM (modulation de largeur d'impulsion) avec une broche GPIO n°27 connectée à un buzzer
vol = 1000 # Définition de la variable "vol" à une valeur de 1000 (qui déterminera le volume du buzzer)

#Gamme3
def MI3(time): #MI
    buzzer.freq(165)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def FA_3 (time): #FA #
    buzzer.freq(185)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
    
def LA3(time): #LA
    buzzer.freq(220)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def LA_3(time): #LA #
    buzzer.freq(233)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
    
def SI3(time): #SI
    buzzer.freq(246)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def SOL_3(time): #SOL#
    buzzer.freq(196)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
 
#Gamme 4
def DO4 (time): #DO
    buzzer.freq(227)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
    
def MI4(time): #MI
    buzzer.freq(329)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def FA_4 (time): #FA#
    buzzer.freq(370)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)

def RE4 (time): #RE
    buzzer.freq(294)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)


def DO_4 (time): #DO#
    buzzer.freq(277)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
    
def LA4 (time): #LA
    buzzer.freq(440)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)
    
def SI4(time): #SI
    buzzer.freq(493)
    buzzer.duty_u16(vol)
    sleep(time)
    buzzer.duty_u16(0)  

    
while True:  

    DO_4(0.15)
    SI3(0.15)
    DO_4(0.45)
    FA_3(0.45)
    sleep(0.8)
    
    RE4(0.15)
    DO_4(0.15)
    RE4(0.2)
    DO_4(0.2)
    SI3(0.5)
    sleep(0.8)
    
    RE4(0.15)
    DO_4(0.15)
    RE4(0.45)
    FA_3(0.45)
    sleep(0.8)
    
    SI3(0.15)
    LA3(0.15)
    SI3(0.25)
    LA3(0.25)
    SOL_3(0.25)
    SI3(0.25)
    LA3(0.8)
    
    DO_4(0.15)
    SI3(0.15)
    DO_4(0.35)
    FA_3(0.4)
    sleep(0.8)
    
    RE4(0.15)
    DO_4(0.15)
    RE4(0.2)
    DO_4(0.2)
    SI3(0.5)
    sleep(0.8)
    
    RE4(0.15)
    DO_4(0.15)
    RE4(0.35)
    FA_3(0.4)
    sleep(0.8)
    
    SI3(0.15)
    LA3(0.15)
    SI3(0.25)
    LA3(0.25)
    SOL_3(0.25)
    SI3(0.25)
    LA3(0.8)
    
    SOL_3(0.15)
    LA3(0.15)
    SI3(0.5)
    
    LA3(0.15)
    SI3(0.15)
    DO_4(0.2)
    SI3(0.2)
    LA3(0.2)
    SOL_3(0.2)
    FA_3(0.3)
    
    RE4(0.3)
    DO_4(1)
    
    DO_4(0.1)
    RE4(0.1)
    DO_4(0.1)
    
    SI3(0.1)
    
    DO_4(1)
