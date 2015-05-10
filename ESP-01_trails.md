# Resultaten tests

## Test Appsaloon-jam

* Model: ESP-01
* default baud: 9600
* geconnecteerd via USB-FDTI chip

Wiring:

* GND van FDTI-bordje
* Vcc van de 3.3V pin op het FDTI-bordje
* TX-TDX
* RX-RXD
* CH_PD naar Vcc hoog getrokken


* Seriele console werkt (AT, AT+RST, AT+GMR), maar na een tijdje lijkt er lag te zijn (resetten helpt dat)
* esptool geeft "Failed to connect"

Firmware version:

    AT+GMR
    0020000903
    compiled @ Dec 15 2014 19:43:31
    AITHINKER-20141206

    OK

