import network
import machine
import socket
import binascii
import dht22
import time

# set in Dingnet dashboard https://dingnet-account.icts.kuleuven.be/platform/
APP_EUI = 'xxxxxxxxxxxxxxxxxx'
APP_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# DHT22_PIN = 28


def join_dingnet(app_eui, app_key):
    lora = network.LoRa(mode=network.LoRa.LORAWAN)
    app_eui = binascii.unhexlify(app_eui)
    app_key = binascii.unhexlify(app_key)

    # connect with OTAA-authentication (only supported method with Dingnet)
    lora.join(activation=network.LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    return lora


def monitor():
    # connected DHT22 data-pin, change if needed
    dht = dht22.device(machine.Pin.exp_board.G28)
    lora = join_dingnet(APP_EUI, APP_KEY)

    print('Trying to join LoRa-network')
    while not lora.has_joined():
        pass

    # create a raw nonblocking LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setblocking(False)

    print('Joined LoRa-network, start monitoring temperature/humidity')

    while True:
        # trigger only happens when DHT22 has new values, 2sec resolution
        # might be needed to change the dht22-lib, if subsequent
        # trigger()-calls keep returning False, see dht22.py in repo and
        # https://github.com/erikdelange/WiPy-2.0-DHT22/issues/1

        if dht.trigger() == True:
            print("RH = {}%  T = {}C".format(dht.humidity, dht.temperature))
            try:
                # send values over LoRaWAN
                s.send(''.join(['H', str(dht.humidity)]))
                s.send(''.join(['T', str(dht.temperature)]))
            except OSError:  # catch/ignore EAGAIN-error
                pass
            time.sleep(1)  # sleep 1 second, avoid EAGAIN duty cycling error?
            # https://forum.pycom.io/topic/2590/oserror-errno-11-eagain
        else:
            print(dht.status)
            print(lora.has_joined())
