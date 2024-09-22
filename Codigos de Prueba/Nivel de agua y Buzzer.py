from machine import Pin, PWM, ADC
import time

#Creacion de variables para pines ADC
adcAgua= ADC(Pin(12,Pin.IN))
adcAgua.atten(ADC.ATTN_11DB)
buzzer=PWM(Pin(15))

#Funcion que mide el nivel de agua
#Cuando el nivel de agua es bajo, el sitema emite una alerta a traves de un buzzer
def agua (adcA,buzzer):
    while True:
        time.sleep(1)
        Nagua= adcA.read_u16()
        print(int(Nagua/1000))
        Vbuzz=int(Nagua/1000)
        if Vbuzz < 48:
            buzzer.freq(1000)
            buzzer.duty_u16(50000)
        else:
            buzzer.duty_u16(0)
print(agua(adcAgua,buzzer))