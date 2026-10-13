import RPi.GPIO as IO
import time
import threading

pin_led1 = 17; pin_led2 = 25
IO.setmode(IO.BCM)
IO.setup([pin_led1, pin_led2], IO.OUT)

# Función objetivo para el Hilo 1
def led1_blink():
    while True:
        IO.output(pin_led1, not IO.input(pin_led1))
        time.sleep(5) # Se suelta el candado GIL aquí

# Función objetivo para el Hilo 2
def led2_blink():
    while True:
        IO.output(pin_led2, not IO.input(pin_led2))
        time.sleep(1)

# Se crean los hilos (como dos trabajadores paralelos)
fil_1 = threading.Thread(target=led1_blink, daemon=True)
fil_2 = threading.Thread(target=led2_blink, daemon=True)

try:
    fil_1.start(); fil_2.start()

    # El programa principal se queda vigilando
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    IO.cleanup()