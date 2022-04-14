#!/usr/bin/env python

import sys
import time
import math

#Import library for envirophat analog sensor
from envirophat import analog

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('************************')

#try except to handle keyboard interrupt
try: 
        #while loop to continuously read data from analog input
        while True:
                #read voltage from analog pins on envirophat
                analog_values = analog.read_all()

                #calculate temperature from analog value on the 0 pin and convert to fahrenheit
                oven_temp = round(((((((analog_values[0]) - 1.25)/0.005) * 9)/ 5.0) + 32),2)

                # Add the value 98.6 to the feed 'Temperature'.
                aio.send('ZeroCool', oven_temp)

                #wait 1 second before cycling through the while loop again
                time.sleep(1)

except KeyboardInterrupt:
        pass