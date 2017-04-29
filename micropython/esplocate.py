import network
import ujson
from mqtt import MQTTClient

sta_if = network.WLAN(network.STA_IF)
aps = sta_if.scan()
aps_data = ujson.dumps(aps)

#c = MQTTClient("huzzah", "broker.hivemq.com", port=1883)
c = MQTTClient("huzzah", "test.mosquitto.org", port=1883)

c.connect()
c.publish(b"mhermans/esplocate/aps", aps_data)
c.disconnect()
