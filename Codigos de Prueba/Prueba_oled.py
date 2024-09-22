#Codigo de prueba para la Pantalla OLED 128x64 con I2C
from machine import Pin, I2C
import ssd1306

# Asignacion del Pin para la pantalla Oled en la ESP32
Entrada = I2C(0, scl=Pin(2, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP))

#Variables para las dimensiones de la pantalla
oled_width = 128
oled_height = 64

#Creacion de la clase SSD1306_I2C() para controlar la pantalla 
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, Entrada)

oled.text("Hello World", 10, 10)      
oled.show()