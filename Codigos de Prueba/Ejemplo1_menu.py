#Ejemplo de menu 1
from machine import Pin, I2C
import ssd1306
from menuoled import MENU_OPTIONS, NAVIGATE_MENU
import time

def eleccion(decenash,unidadesh):
    for x in decenash:
        if x == True:
            decena= int(x)
        else:
            pass
    for x in unidadesh:
        if x == True:
            unidad= int(x)
        else:
            pass
    return decena*10+unidad    
def show_main_menu():
    print("Menú principal")
    main_menu.draw()


def porcentaje_humedad():
    print("Opción 1 seleccionada")
    secondary_menu.draw()
    
def unidades():
    print("Opción 1 seleccionada")
    unidadesh.draw()
    
    
   
def tiempo_revision():
    print("Opción 1 seleccionada")
    secondary_menu.draw()
    
def reinicio():
    print("Opción 1 seleccionada")
    secondary_menu.draw()


def simple_text():
    print("Opción 2 seleccionada")

    simple_text_menu.draw()
    oled.text("Esta es la opcion", 0, 16)
    oled.text("de texto simple", 0, 24)
    oled.show()


def show_icon():
    print("Opción 3 seleccionada")

    show_icon_menu.draw()
    oled.blit(show_icon_menu.openIcon('config'), 20, 16)
    oled.show()


def option_1_1():
    print("Opción 1_1 seleccionada")
    option_1_1_menu.draw()
    oled.text("NADA", 30, 18)
    oled.show()


# Crear un OLED
Entrada = I2C(0, scl=Pin(2, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, Entrada)

# Crear un menú principal
main_menu = MENU_OPTIONS(oled)

# Agregar elementos a main_menu
main_menu.add_option("Porcentaje de humedad", porcentaje_humedad)
main_menu.add_option("Tiempo de revision", tiempo_revision)
main_menu.add_option("Reinicio", reinicio)


# Crea menú de la opción 1
porcentaje_humedad = MENU_OPTIONS(oled)

# Agregar elementos a menu_option_1
porcentaje_humedad.add_option("Selecciona porcentaje de humedad",simple_text)

decenash = MENU_OPTIONS(oled)

decenash.add_option(0, unidades)
decenash.add_option(1, unidades)
decenash.add_option(2, unidades)
decenash.add_option(3, unidades)
decenash.add_option(4, unidades)
decenash.add_option(5, unidades)
decenash.add_option(6, unidades)
decenash.add_option(7, unidades)
decenash.add_option(8, unidades)
decenash.add_option(9, unidades)

unidadesh = MENU_OPTIONS(oled)

unidadesh.add_option(0, show_main_menu)
unidadesh.add_option(1, show_main_menu)
unidadesh.add_option(2, show_main_menu)
unidadesh.add_option(3, show_main_menu)
unidadesh.add_option(4, show_main_menu)
unidadesh.add_option(5, show_main_menu)
unidadesh.add_option(6, show_main_menu)
unidadesh.add_option(7, show_main_menu)
unidadesh.add_option(8, show_main_menu)
unidadesh.add_option(9, show_main_menu)

print(eleccion(decenas,unidades))


# Crea menú de la opción texto simple
 
tiempo_revision.add_option("Selecciona el tiempo que habra entre cada revisión",show_())

tiempo_opcion = MENU_OPTIONS(oled)

tiempo_opcion.add_option(0)
tiempo_opcion.add_option(1)
tiempo_opcion.add_option(2)
tiempo_opcion.add_option(3)
tiempo_opcion.add_option(4)
tiempo_opcion.add_option(5)
tiempo_opcion.add_option(6)
tiempo_opcion.add_option(7)
tiempo_opcion.add_option(8)
tiempo_opcion.add_option(9)

while True:       
    for x in tiempo_opcion:
        if x == True:
            tiempo_r=str(x)
            tiempo_r=+(tiempo_r)
        else:
            pass
        
tiempo_r=int(tiempo_r)    
    
# Agregar elementos a texto simple
tiempo_revision.add_option("Menu principal", show_main_menu)


menu_list = [main_menu,
             decenash,
             unidadesh,
             show_icon_menu,
             option_1_1_menu]

menu = NAVIGATE_MENU(menu_list)

# Configura botones de navegación

abajo = Pin(19, Pin.OUT, Pin.PULL_DOWN)
arriba = Pin(21, Pin.OUT, Pin.PULL_DOWN)
selector = Pin(18, Pin.OUT, Pin.PULL_DOWN)
abajo.on()
arriba.on()
selector.on()


# Dibujar el menú
main_menu.draw()

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
        time.sleep(0.5)
    print(arriba.value(),abajo.value(),selector.value())

