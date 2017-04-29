import time
import machine, neopixel
from mqtt import MQTTClient

np = neopixel.NeoPixel(machine.Pin(15), 16)

# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))
    topic = topic.decode('UTF-8')
    msg = msg.decode('UTF-8')
    
    nlight = int(topic.split('/')[2])
    r, g, b = str(msg).split(',')

    np[nlight] = (int(r), int(g), int(b))
    np.write()

def main(server="test.mosquitto.org"):
    c = MQTTClient("umqtt_clientc", server)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"mhermans/lights/#")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()
