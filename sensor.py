import dht11
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


try:
    while True:    
        instance=dht11.DHT11(pin=4)
        result = instance.read()
        print 'temperature'+str(result.temperature)
        print 'humidity'+str(result.humidity)
        time.sleep(2)
except KeyboardInterrupt:
    pass