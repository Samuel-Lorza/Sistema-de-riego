#Primer codigo de prueba del sistema
#Distintos imports de bibliotecas para las funciones del sistema
from machine import Pin, PWM, ADC, RTC, I2C, deepsleep
import time, ssd1306
from menuoled import MENU_OPTIONS, NAVIGATE_MENU
import esp32

def show_main_menu():
    print("Menú principal")
    main_menu.draw()

def humedad_option():
    print("Opción 1 seleccionada")
    humedad_opcion.draw()


def tiempo_option():
    print("Opción 2 seleccionada")
    tiempo_revision.draw()
    
def humedad25_elegida():
    global humedad
    humedad=(25)
    main_menu.draw()
    return humedad
def humedad50_elegida():
    global humedad
    humedad= 50
    main_menu.draw()
    return humedad
def humedad75_elegida():
    global humedad
    humedad= 75
    main_menu.draw()
    return humedad
def humedad100_elegida():
    global humedad
    humedad= 90
    main_menu.draw()
    return humedad
def tiempo_elegida():
    global tiempo
    tiempo= 1
    main_menu.draw()
    return tiempo
def tiempo1_elegida():
    global tiempo
    tiempo= 60
    main_menu.draw()
    return tiempo
def tiempo2_elegida():
    global tiempo
    tiempo= 120
    main_menu.draw()
    return tiempo

def agua (adcA,buzzer):
    while True:
        bomba=PWM(Pin(13))
        bomba.deinit()
        time.sleep(2)
        Nagua= adcA.read_u16()
        Vbuzz=int(Nagua/1000)
        if Vbuzz < 48:
            buzzer.init()
            buzzer.freq(1000)
            buzzer.duty_u16(50000)
        else:
            buzzer.deinit()
            break
            
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
        else:
            bomba.deinit()
            contador= contador + 1
            if (contador==3):
                break
        time.sleep(0.5)

#Zona donde se establecen las variables
        
    #Pin del sensor de humedad
adcH= ADC(Pin(33,Pin.IN))
adcH.atten(ADC.ATTN_11DB)
    #Pin de la bomba de agua
PinBomba=Pin(13)
bomba=PWM(PinBomba)
bomba.deinit()
    #Pin del nivel de agua
adcAgua= ADC(Pin(12,Pin.IN))
adcAgua.atten(ADC.ATTN_11DB)
    #Asignación del buzzer
PinBuzzer=Pin(15)
buzzer=PWM(PinBuzzer)
buzzer.deinit()
    #Asignacion del Real Time Clock
rtc = RTC()
mem = rtc.memory()
    #Botones
        # Configura botones de navegación
abajo = Pin(19, Pin.OUT, Pin.PULL_DOWN)
arriba = Pin(21, Pin.OUT, Pin.PULL_DOWN)
selector = Pin(18, Pin.OUT, Pin.PULL_DOWN)
abajo.on()
arriba.on()
selector.on()
humedad,tiempo=-1,-1



#Creacion de la pantalla OLED, sus menus, opciones etc.
Entrada = I2C(0, scl=Pin(2, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, Entrada)

# Crear un menú principal
main_menu = MENU_OPTIONS(oled)

# Agregar elementos a main_menu
main_menu.add_option("Porcentaje de humedad", humedad_option)
main_menu.add_option("Tiempo de revision", tiempo_option)
#main_menu.add_option("Reinicio", Reinicio)


# Crea menú de la humedad
humedad_opcion = MENU_OPTIONS(oled)

# Agregar elementos al menu de la humedad
humedad_opcion.add_option("Menu principal", show_main_menu)
humedad_opcion.add_option("25%", humedad25_elegida)
humedad_opcion.add_option("50%", humedad50_elegida)
humedad_opcion.add_option("75%", humedad75_elegida)
humedad_opcion.add_option("90%", humedad100_elegida)

# Crear menú del tiempo entre revisiones
tiempo_revision = MENU_OPTIONS(oled)

# Agregar elementos al menú del tiempo entre revisiones
tiempo_revision.add_option("Menu principal", show_main_menu)
tiempo_revision.add_option("Cada 30 min", tiempo_elegida)
tiempo_revision.add_option("1 hora", tiempo1_elegida)
tiempo_revision.add_option("2 horas", tiempo2_elegida)

menu_list = [main_menu,
             humedad_opcion,
             tiempo_revision,
             ]
#Parametro para moverse en el menu
menu = NAVIGATE_MENU(menu_list)

# Dibujar el menú
main_menu.draw()

#Configuracion de las variables para hacer funcionar los botones
print(humedad, tiempo,(humedad>0) and (tiempo>0),(humedad>0), (tiempo>0))    
while True:
        if arriba.value()==0:
            print("Arriba")
            menu.navigate("up")
            time.sleep(0.5)

        if abajo.value()==0:
            print("Abajo")
            menu.navigate("down")
            time.sleep(0.5)

        if selector.value()==0:
            print("Seleccionar")
            menu.select()
            selector.value(1)
            time.sleep(0.5)
            
        if mem:
            # Convertir los bytes a cadena y luego separarlos
            datos = mem.decode().split(',')
            humedad = int(datos[0])  # Primer valor es el contador
            tiempo = int(datos[1])         # Segundo valor es el estado
        if ((int(humedad)>0) and (int(tiempo>0))):
            # Guardar las variables en la memoria RTC como una cadena combinada
            datos_a_guardar = f"{humedad},{tiempo}".encode()
            rtc.memory(datos_a_guardar)
            #Despues de la configuración del sistema, este ciclo hara que todo el tiempo se revisen los parametros        
            agua(adcAgua,buzzer)
            print("salio de la revision X")
            PorcentajeHumedad (adcH,bomba,humedad)
            print("salio de la revision")
            adcH= ADC(Pin(33, Pin.IN, value=0, hold=True))
            adcAgua= ADC(Pin(12,Pin.IN,value=0, hold=True))
            PinBuzzer=Pin(15, Pin.OUT, value=0, hold=True)
            PinBomba=Pin(13, Pin.OUT, value=0, hold=True)
            print("Entrando al deepsleep")
            deepsleep(10000)#tiempo*60000)
    
    
    
    