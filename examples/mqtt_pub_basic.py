from mqtt import MQTTClient


#c = MQTTClient("huzzah", "broker.hivemq.com", port=1883)
c = MQTTClient("huzzah", "test.mosquitto.org", port=1883)

c.connect()
c.publish(b"mhermans/lights/1", b"0,0,0")
c.disconnect()
