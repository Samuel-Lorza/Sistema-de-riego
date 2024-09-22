#Codigo del Menu del sistema

#Diferrentes bibliotecas utilizadas para las funciones del menu y la pantalla
from machine import Pin, I2C
import ssd1306
from menuoled import MENU_OPTIONS, NAVIGATE_MENU
import time

#Creacion de funciones, que son las acciones que van a realizar las opciones del menu
def show_main_menu():
    print("Menú principal")
    main_menu.draw()


def humedad_option():
    print("Opción 1 seleccionada")
    humedad_opcion.draw()


def tiempo_option():
    print("Opción 2 seleccionada")
    tiempo_revision.draw()
    

def show_icon():
    print("Opción 3 seleccionada")

    show_icon_menu.draw()
    oled.blit(show_icon_menu.openIcon('config'), 20, 16)
    oled.show()


def humedad25_elegida():
    humedad= 25
    main_menu.draw()
    return humedad
def humedad50_elegida():
    humedad= 50
    main_menu.draw()
    return humedad
def humedad75_elegida():
    humedad= 75
    main_menu.draw()
    return humedad
def humedad100_elegida():
    humedad= 100
    main_menu.draw()
    return humedad
def tiempo_elegida():
    tiempo= 30
    main_menu.draw()
    return tiempo
def tiempo1_elegida():
    tiempo= 1
    main_menu.draw()
    return tiempo
def tiempo2_elegida():
    tiempo= 2
    main_menu.draw()
    return tiempo

# Crear una variable para la pantalla OLED, donde se va a mostrar el menu
Entrada = I2C(0, scl=Pin(2, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, Entrada)

# Crear un menú principal
main_menu = MENU_OPTIONS(oled)

# Agregar elementos a menu principal
main_menu.add_option("Porcentaje de humedad", humedad_option)
main_menu.add_option("Tiempo de revision", tiempo_option)
#main_menu.add_option("Icono", show_icon)


# Crea menú del porcentaje de humedad
humedad_opcion = MENU_OPTIONS(oled)

# Agregar elementos al menu de porcentaje de humedad
humedad_opcion.add_option("Menu principal", show_main_menu)
humedad_opcion.add_option("0 - 25%", humedad25_elegida)
humedad_opcion.add_option("25 - 50%", humedad50_elegida)
humedad_opcion.add_option("50 - 75%", humedad75_elegida)
humedad_opcion.add_option("75 - 100%", humedad100_elegida)

# Crea menú del tiempo de revision
tiempo_revision = MENU_OPTIONS(oled)

# Agregar elementos al menu de tiempo de revision
tiempo_revision.add_option("Menu principal", show_main_menu)
tiempo_revision.add_option("Cada 30 min", tiempo_elegida)
tiempo_revision.add_option("1 hora", tiempo1_elegida)
tiempo_revision.add_option("2 horas", tiempo2_elegida)

#Crear una lista con los menus anteriores, que sirve como parametro para la funcion NAVIGATE_MENU() 
menu_list = [main_menu,
             humedad_opcion,
             tiempo_revision,
             ]
#Funcion que permite navegar por los menus, a continuacion
menu = NAVIGATE_MENU(menu_list)

# Configura botones de navegación
abajo = Pin(19, Pin.OUT, Pin.PULL_DOWN)
arriba = Pin(21, Pin.OUT, Pin.PULL_DOWN)
selector = Pin(18, Pin.OUT, Pin.PULL_DOWN)
abajo.on()
arriba.on()
selector.on()


# Dibujar el menu
main_menu.draw()

#Establecer el mecanismo para navegar por los menus a traves de los botones
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
