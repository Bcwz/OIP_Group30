from sense_hat import SenseHat  
import time  
import sys   
  
# --------- User Settings ---------
MINUTES_BETWEEN_SENSEHAT_READS = 0.1
# ---------------------------------

sense = SenseHat()  
  
while True:
  # Read the sensors
  temp_c = sense.get_temperature()
  humidity = sense.get_humidity() 
  pressure_mb = sense.get_pressure() 

  # Format the data
  #temp_f = temp_c * 9.0 / 5.0 + 32.0
  #temp_f = float("{0:.2f}".format(temp_f))
  temp_c = float("{0:.2f}".format(temp_c))
  humidity = float("{0:.2f}".format(humidity))

  # Print and stream
  print("Temperature(C): ", temp_c)
  print("Humidity(%): ", humidity)
  time.sleep(60*MINUTES_BETWEEN_SENSEHAT_READS)
