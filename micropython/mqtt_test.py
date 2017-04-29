from network import WLAN 
from mqtt import MQTTClient 
import machine 
import time 
def settimeout(duration):  
   pass 
client = MQTTClient("huzzah", "io.adafruit.com",user="mhermans", password="ef94dea6d1cd415f9dd4ebb0e06d69a7", port=1883)  
client.settimeout = settimeout 
client.connect() 
while True: 
    print("Sending ON") 
    client.publish("/accesspoints", "ON")    
    time.sleep(1) 
    print("Sending OFF") 
    client.publish("/accesspoints", "OFF")
    time.sleep(1) 
