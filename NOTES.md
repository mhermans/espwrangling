# Notes

## Micropython notes

Get REPL-prompt over serial:

    sudo dmesg | grep tty 
    screen /dev/ttyUSB0 115200


### Setup 

How to check currently installed firmware version?

ctrl-d in REPL => soft reboot

    MicroPython 8785822 on 2016-10-06; LoPy with ESP32

    import uos
    uos.uname()

    (sysname='ESP32', nodename='ESP32', release='0.9.0b', version='1f7bdfd on 2016-10-09', machine='WiPy with ESP32')
    (sysname='WiPy', nodename='WiPy', release='1.9.2.b2', version='v1.8.6-796-g489fafa0 on 2017-10-15', machine='WiPy with ESP32')

Check that board is in P32-ground, connect on terminal, press reset => 

    POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
    waiting for download


    workon micropython-test
    pip install adafruit-ampy
    pip install esptool


Enable non-root access to /dev/ttyUSB0 (users in dailout group have R/W access to devices)

    sudo usermod -a -G dialout mhermans



Error flashing firmware

    rst:0x1 (POWERON_RESET),boot:0x3 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
    waiting for download



wlan.connect('mushroomservice', auth = (wlan.WPA2, 'IKM@geertrui3'))

generate lopy DevEUI based on MAC:

    import binascii
    from network import LoRa
    lora = LoRa(mode=LoRa.LORAWAN)
    binascii.hexlify(lora.mac())

## PCB-design inspiration

* [design with voltage regulator & jumper](http://ciphersink.net/post/18)
* [design with voltage regulator, capacitors, etc.](http://makezine.com/2015/04/01/designing-breadboard-adaptor-5-esp8266-microcontroller/)
* [design 2-button reset/programming mode](http://www.xess.com/blog/esp8266-reflash/)
* [Adafruit breakout board](https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout/overview)
* [notes on 5V-3.3V level shiting strategies](http://jamesreubenknowles.com/level-shifting-stragety-experments-1741)


## Arduino 

* [Example Arduino-sketch with software serial](https://github.com/soynerdito/ESP8266-MQTT/blob/master/examples/ESP8266Echo/ESP8266Echo.ino)


## General notes

* [ESP models reference](http://l0l.org.uk/2014/12/esp8266-modules-hardware-guide-gotta-catch-em-all/)
* [walkthrough](http://www.labradoc.com/i/follower/p/notes-esp8266)
* [reference](https://nurdspace.nl/ESP8266)
* [reference](wiki.iteadstudio.com/ESP8266_Serial_WIFI_Module)
* [my ESP8266 bookmarks](https://pinboard.in/u:mhermans/t:esp8266/)


## Tools

* [esptool](https://github.com/themadinventor/esptool/)
* [nodeMCU](http://nodemcu.com/index_en.html)
* [ESP8266 Arduino add-on](https://github.com/sandeepmistry/esp8266-Arduino)



    curl -O https://raw.githubusercontent.com/micropython/micropython-lib/2164c88483f47117ba1ce9128753599f819c658b/umqtt.simple/umqtt/simple.py

    sudo ampy --port /dev/ttyUSB0 put simple /mqtt.py




curl -O https://raw.githubusercontent.com/micropython/micropython-lib/master/umqtt.simple/umqtt/simple.py
curl -O https://raw.githubusercontent.com/micropython/micropython-lib/master/urequests/urequests.py


http://www.hivemq.com/demos/websocket-client/

https://github.com/micropython/micropython-lib/tree/master/umqtt.simple


mosquitto_pub -h test.mosquitto.org -t "mhermans/lights/1" -m "0,0,0"
mosquitto_sub -h test.mosquitto.org -t "mhermans/lights/#" -v




https://requestb.in/

https://lab.whitequark.org/notes/2016-10-20/controlling-a-gpio-through-an-esp8266-based-web-server/

sudo ampy --port /dev/ttyUSB0 put mqtt.py


MQTT nonblocking example https://forum.micropython.org/viewtopic.php?f=16&t=3283

https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#timers
from machine import Timer
tim = Timer(-1)
tim.init(period=500, mode=Timer.PERIODIC, callback=lambda t: p0.value(not p0.value()))
tim.deactivate()

<<<<<<< HEAD

# Setup micropython tools

Create a virtual environment and install tools

    virtualenv3 ~/lib/virtualenvs/espenv
    source ~/lib/virtualenvs/espenv/bin/activate

    pip3 install adafruit-ampy
    pip3 install esptool


    curl -O http://micropython.org/resources/firmware/esp8266-20170108-v1.8.7.bin
    dmesg | grep cp210x
    esptool.py --port /dev/ttyUSB0 erase_flash
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin 

    screen /dev/ttyUSB0 115200

# MQTT

sudo apt-get install mosquitto-clients

=======
# LoPy notes

updated to 1.15.0.b1


# u-nummer als login voor VPN
apt-get install openconnect
openconnect -v --juniper https://extranet.kuleuven.be/b
ping icts-p-dingnet-account-1.lnx.icts.kuleuven.be
mosquitto_sub -h 'icts-p-dingnet-account-1.lnx.icts.kuleuven.be' -p 1883 -t 'app_u0062125/#' -d -u u0062125 -P 10bfde7dfffceb74911d5c846de4237f


>>> import socket
>>> s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
>>> s.setblocking(False)
>>> s.send('aa')
>>>>>>> 7752822782ae42550d35f67069f144afbcd186d8

