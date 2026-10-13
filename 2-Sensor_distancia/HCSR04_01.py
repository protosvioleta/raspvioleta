import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG= 17
ECHO=25
GPIO.setup(TRIG GPIOOUT)
GPIO.setup(ECHO, GPIO.IN)

def mesura_distancia():

	GPIO.output(TRIG True)
	time.sleep(0.00001)
	GPIO.output(TRIG False)
	while GPIQ.input(ECHO) == 0:
		start_time = time.time()
	while GPIO.input(ECHO) == 1:
		end_time = time.time()
	temps_total = end_time - start_time
	distancia = (temps_total * 34300) /2 # Resultat en cm
	return distancia

try:
	while True:
		distancia = mesura_distancia()
		print(f"Distancia: {distancia :. 2f} cm")
		time.sleep(1)
except KeyboardInterrupt
	print("Mesura aturada per usuari")
	GPIO.cleanup()