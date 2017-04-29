from simple import MQTTClient

# Test reception e.g. with:
# mosquitto_sub -t foo_topic

c = MQTTClient("huzzah", "broker.hivemq.com", port=1883)
#user="mhermans", 
#password="ef94dea6d1cd415f9dd4ebb0e06d69a7", 
#port=1883)


c.connect()
c.publish(b"mhermans/lights/1", b"255,0,0")
c.disconnect()
