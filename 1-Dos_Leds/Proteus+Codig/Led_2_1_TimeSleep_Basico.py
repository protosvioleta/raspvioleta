import RPi.GPIO as GPIO
import time

# Declaración de variables globales
led1 = 17
led2 = 25
pausa = 1

# Definición de función para agrupar lógica
def estat(estat1, estat2, delay):
    GPIO.output(led1, estat1)
    GPIO.output(led2, estat2)
    time.sleep(delay) # PUNTO DE BLOQUEO: La CPU se congela aquí

GPIO.setmode(GPIO.BCM)
GPIO.setup([led1, led2], GPIO.OUT)

try:
    while True: # Bucle infinito principal
        estat(GPIO.HIGH, GPIO.LOW, pausa)
        estat(GPIO.LOW, GPIO.HIGH, pausa)

except KeyboardInterrupt:
    # Excepción para liberar pines si el usuario presiona Ctrl+C
    GPIO.cleanup()