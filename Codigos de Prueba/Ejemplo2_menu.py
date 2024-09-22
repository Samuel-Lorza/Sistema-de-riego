#Ejemplo de menu 2

from machine import Pin, I2C
import ssd1306
from menuoled import MENU_OPTIONS, NAVIGATE_MENU
import time


def show_main_menu():
    print("Menú principal")
    main_menu.draw()


def humedad_option():
    print("Opción 1 seleccionada")
    humedad_opcion.draw()


def tiempo_option():
    print("Opción 2 seleccionada")

    tiempo_revision.draw()
    oled.text("Esta es la opcion", 0, 16)
    oled.text("de texto simple", 0, 24)
    oled.show()


def show_icon():
    print("Opción 3 seleccionada")

    show_icon_menu.draw()
    oled.blit(show_icon_menu.openIcon('config'), 20, 16)
    oled.show()


def option_elegida():
    humedad= 25
    return humedad


# Crear un OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Crear un menú principal
main_menu = MENU_OPTIONS(oled)

# Agregar elementos a main_menu
main_menu.add_option("Porcentaje de humedad", humedad_option())
main_menu.add_option("Tiempo de revision", tiempo_option())
#main_menu.add_option("Icono", show_icon)


# Crea menú de la opción 1
humedad_opcion = MENU_OPTIONS(oled)

# Agregar elementos a menu_option_1
humedad_opcion.add_option("Menu principal", show_main_menu)
humedad_opcion.add_option("0 - 25%", option_1_1)
humedad_opcion.add_option("25 - 50%", option_1_1)
humedad_opcion.add_option("50 - 75%", option_1_1)
humedad_opcion.add_option("75 - 100%", option_1_1)
# Crea menú de la opción texto simple
tiempo_revision = MENU_OPTIONS(oled)

# Agregar elementos a texto simple
tiempo_revision.add_option("Menu principal", show_main_menu)
tiempo_revision.add_option("Cada 30 min", show_main_menu)
tiempo_revision.add_option("1 hora", show_main_menu)
tiempo_revision.add_option("2 horas", show_main_menu)


show_icon_menu = MENU_OPTIONS(oled)

 Agregar elementos a texto simple
show_icon_menu.add_option("Menu principal", show_main_menu)


option_1_1_menu = MENU_OPTIONS(oled)

 Agregar elementos a texto simple
option_1_1_menu.add_option("Menu principal", show_main_menu)


menu_list = [main_menu,
             humedad_opcion,
             tiempo_revision,
             ]

menu = NAVIGATE_MENU(menu_list)

# Configura botones de navegación
button_down = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_up = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_select = Pin(15, Pin.IN, Pin.PULL_DOWN)


# Dibujar el menú
main_menu.draw()

while True:

    if button_up.value():
        print("Arriba")
        menu.navigate("up")
        time.sleep(0.5)

    if button_down.value():
        print("Abajo")
        menu.navigate("down")
        time.sleep(0.5)

    if button_select.value():
        print("Seleccionar")
        menu.select()
        time.sleep(0.5)
