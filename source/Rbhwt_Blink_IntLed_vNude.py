from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT) # Funciona igual en Pico _, Pico 2, Pico W o en Pico 2W

print("el LED interno comienza a parpadear...")
while True:
    pin.toggle() # alterna el estado si 1 -> 0 y si 0 -> 1
    sleep(1) # espera 'dormido' 1 segundo
