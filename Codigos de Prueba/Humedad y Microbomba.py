#Codigo de prueba para el sensor de humedad y la microbomba que riega la planta

from machine import Pin, PWM, ADC
import time

#Creacion de variables para la humedad
adcH= ADC(Pin(33,Pin.IN))
adcH.atten(ADC.ATTN_11DB)

#Asignacionde variables para la bomba de agua
bomba=PWM(Pin(13))
bomba.deinit()

#Entrada de teclado para la prueba del sensor de humedad y la bomba
H_usuario=int(input("Digite el porcentaje de humedad "))
contador=int(0)

#funcion que evalua el porcentaje de humedad de la planta para regarla
def PorcentajeHumedad (adcH,bomba,H_usuario):
    contador=int(0)
    while True:
        Nhumedad= adcH.read_u16()
        Nhumedad_real=(65535-Nhumedad)
        Nhumedadp=int(Nhumedad_real/655.35)
        if (Nhumedadp < H_usuario-5):
            bomba.init()
            bomba.freq(500)
            bomba.duty_u16(40000)
            #print ("Entro if")
        else:
            print ("Entro else")
            bomba.deinit()
            contador= contador + 1
            print(Nhumedadp, "  ", Nhumedadp < H_usuario, " ", contador)
            if (contador==3):
                break
        print(Nhumedadp, "  ", Nhumedadp < H_usuario, "O")
        time.sleep(1)
#Llamar al afuncion        
PorcentajeHumedad(adcH,bomba,H_usuario)