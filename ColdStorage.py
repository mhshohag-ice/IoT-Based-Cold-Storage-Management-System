
import sys
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import urllib2

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Motor1A = 16
Motor1B = 18
Motor1E = 22
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

myAPI = "NSWUGLOJIDCEKSUE"
myDelay = 15
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
Light = 1000

GPIO.setup(11,GPIO.IN)
GasPin = 11
DHT_1 = 11
DHT_2 = 4
FireDetection = 10
while True:
    FireDetection = GPIO.input(GasPin)
    hum , temp = Adafruit_DHT.read_retry(DHT_1,DHT_2)
    f = urllib2.urlopen(baseURL +"&field1=%s&field2=%s&field3=%s" % (temp, hum, FireDetection))
    print(temp)
    print(hum)
    print(FireDetection)
    if temp>30:
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
    else:
        GPIO.output(Motor1E,GPIO.LOW)
GPIO.cleanup();

