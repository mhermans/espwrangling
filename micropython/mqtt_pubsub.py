from mqtt import MQTTClient
import machine
import time
import ubinascii
from machine import Timer

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SERVER = "test.mosquitto.org"
#SERVER = "broker.hivemq.org"
PORT = 1883

def push_heartbeat():
    c_mqtt.connect()
    c_mqtt.publish(b"mhermans/heartbeat", b'1')
    c_mqtt.disconnect()

global c_mqtt
c_mqtt = MQTTClient(client_id = CLIENT_ID, server = SERVER, port = PORT)

while True:
    c_mqtt.check_msg()


# main loop
# pub: heartbeat every 5sec.
# sub: print every msg immediatly 
