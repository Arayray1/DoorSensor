import Adafruit_BBIO.ADC as ADC
import time
import requests

ADC.setup()
while (1==1):
    value = ADC.read_raw("AIN1")
    distanceIn = value/6.23
    # print "raw value: " + str(value)
    # print "distanceIn: " + str(distanceIn)
    # time.sleep(2)
    try:
        if distanceIn < 20:
            r = requests.post("http://192.168.20.88:80/status", data={'status':"here"})
            print "Someone is here"
        else:
            r = requests.post("http://192.168.20.88:80/status", data={'status':"not here"})
        # print "No one is here"
    except KeyboardInterrupt:
        print ("Quitting")
        quit()
    except:
        print ("Oops failed to post to the listeners. Is the listener running?")
