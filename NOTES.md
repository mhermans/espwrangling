# Notes

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


    curl -O http://micropython.org/resources/firmware/esp8266-20170108-v1.8.7.bin
    dmesg | grep cp210x
    esptool.py --port /dev/ttyUSB0 erase_flash
    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin 

    screen /dev/ttyUSB0 115200

    curl -O https://raw.githubusercontent.com/micropython/micropython-lib/2164c88483f47117ba1ce9128753599f819c658b/umqtt.simple/umqtt/simple.py

    sudo ampy --port /dev/ttyUSB0 put simple /mqtt.py




curl -O https://raw.githubusercontent.com/pycom/pycom-libraries/master/examples/mqtt/mqtt.py

curl -O https://raw.githubusercontent.com/micropython/micropython-lib/master/umqtt.simple/umqtt/simple.py

http://www.hivemq.com/demos/websocket-client/

https://github.com/micropython/micropython-lib/tree/master/umqtt.simple


mosquitto_pub -h test.mosquitto.org -t "mhermans/lights/1" -m "0,0,0"
mosquitto_sub -h test.mosquitto.org -t "mhermans/lights/#" -v


curl -O https://raw.githubusercontent.com/micropython/micropython-lib/master/urequests/urequests.py


https://requestb.in/

https://lab.whitequark.org/notes/2016-10-20/controlling-a-gpio-through-an-esp8266-based-web-server/
