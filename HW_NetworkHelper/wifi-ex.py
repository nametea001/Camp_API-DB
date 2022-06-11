from machine import UART, Pin
from NetworkHelper import NetworkHelper
import time
import sys


def wifi():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("RPi-Pico MicroPython Ver:", sys.version)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    esp8266_at_ver = None
    print("StartUP", con.startUP())
    # print("ReStart",con.reStart())
    print("StartUP", con.startUP())
    print("Echo-Off", con.echoING())
    print("\r\n\r\n")
    esp8266_at_ver = con.getVersion()
    if esp8266_at_ver != None:
        print(esp8266_at_ver)
    print("\r\n\r\n")
    wifimode = con.getCurrentWiFiMode()
    print(f"WIFI mode : {wifimode}")
    if(wifimode != "STA"):
        con.setCurrentWiFiMode(mode=1)
        wifimode = con.getCurrentWiFiMode()
        print(f"WIFI mode : {wifimode}")
    print("\r\n\r\n")
    """
    Connect with the WiFi
    """
    ssid = "Sirichai"  # wifi name
    pwd = "0903319646"  # password
    print("Try to connect with the WiFi..")
    timeout = 0
    # default delay wifi delay 2 sec
    while timeout < 6:
        if "WIFI CONNECTED" in con.connectWiFi(ssid, pwd):
            print("ESP8266 connect with the WiFi..")
            return True
            break
        else:
            print(".")
            timeout += 1
            time.sleep(0.5)
    if timeout >= 6:
        print("Timeout connect with the WiFi")
        return False

con = NetworkHelper()
wifiCon = wifi()
