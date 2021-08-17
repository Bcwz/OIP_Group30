from sense_hat import SenseHat  
import time  
import sys

sense = SenseHat()

def temperature():
    temp_c = sense.get_temperature()
    temp_c = float("{0:.2f}".format(temp_c))
    print("Temperature(C): ", temp_c)
    
def humidity():
    humidity = sense.get_humidity()
    humidity = float("{0:.2f}".format(humidity))
    print("Humidity(%): ", humidity)
    
def temp_Humidity():
    temp_c = sense.get_temperature()
    humidity = sense.get_humidity()
    temp_c = float("{0:.2f}".format(temp_c))
    humidity = float("{0:.2f}".format(humidity))
    print("Temperature(C): ", temp_c)
    print("Humidity(%): ", humidity)
    
#temperature()
#humidity()
#temp_Humidity()