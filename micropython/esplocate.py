import network
import ujson
import ubinascii
from mqtt import MQTTClient

sta_if = network.WLAN(network.STA_IF)
aps = sta_if.scan()

aps_data = []
for ap in aps:
    record = {}
    record['ssid'] = ap[0]
    record['bssid'] = ubinascii.hexlify(ap[1])
    #record['security'] = ap[2]
    record['rssi'] = ap[3]
    
    aps_data.append(record)

aps_data = ujson.dumps(aps_data)

#c = MQTTClient("huzzah", "broker.hivemq.com", port=1883)
c = MQTTClient("huzzah", "test.mosquitto.org", port=1883)

c.connect()
c.publish(b"mhermans/esplocate/aps", aps_data)
c.disconnect()
