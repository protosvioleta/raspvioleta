import RPi.GPIO as IO
import time
import multiprocessing

pin_led1 = 17; pin_led2 = 25

def led1_blink():
    while True:
        IO.output(pin_led1, not IO.input(pin_led1))
        time.sleep(5)

def led2_blink():
    while True:
        IO.output(pin_led2, not IO.input(pin_led2))
        time.sleep(1)

# Protección obligatoria para evitar que los clones se clonen a sí mismos infinitamente
if __name__ == '__main__':
    IO.setmode(IO.BCM)
    IO.setup([pin_led1, pin_led2], IO.OUT)

    # Bifurcación: Asignación de procesos independientes
    proc_1 = multiprocessing.Process(target=led1_blink)
    proc_2 = multiprocessing.Process(target=led2_blink)

    try:
        proc_1.start(); proc_2.start()
        
        # El programa padre bloquea su avance hasta que los hijos terminen
        proc_1.join(); proc_2.join()
        
    except KeyboardInterrupt:
        # Clausura forzosa de los subprocesos aislados
        proc_1.terminate()
        proc_2.terminate()
        IO.cleanup()