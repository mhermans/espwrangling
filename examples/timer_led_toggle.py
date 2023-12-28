# ######################### #
# Blink build-in Huzzah led #
# ######################### #

from machine import Timer, Pin
p0 = Pin(0, Pin.OUT)
tim = Timer(-1)
tim.init(period=500, 
    mode=Timer.PERIODIC, callback=lambda t: p0.value(not p0.value()))
