import machine
import time

# Huzzah has build-in led at 0
led = machine.Pin(0, machine.Pin.OUT)

# toggle led
while True:
    led.value(not led.value())
    time.sleep(0.5) 
