import network
import time
import neopixel
import machine

np = neopixel.NeoPixel(machine.Pin(15), 16)

sta_if = network.WLAN(network.STA_IF)
aps = sta_if.scan()
strenghts = [abs(ap_data[3]) for ap_data in aps]
mean_strength = sum(strenghts)/len(strenghts)
ss_strenghts = [round((strength - mean_strength)**2) for strength in strenghts]

#for i, ap_data in enumerate(aps[1:16]):
for i, strenght in enumerate(ss_strenghts[1:16]):
    #np[i] = (ap_data[3], 0, 0)
    np[i] = (0, strenght, 0)
    #print(abs(ap_data[3]))
    print(strenght)
np.write()

