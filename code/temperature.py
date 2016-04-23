import os
import time
from w1thermsensor import W1ThermSensor

sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0000052cc99d")# internal sensor 
sensor2 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000004ce9b41")# external sensor
temp1 = int(round(sensor1.get_temperature()))# makes an int from the temperature
temp2 = int(round(sensor2.get_temperature()))# makes an int from the temperature

# opening output file and write colom information
outputfile = "/home/pi/temperature.csv"
dataFile_sensor = open( outputfile, 'a')
dataFile_sensor.write("Date" + "," + "Time" + "," + "Internal" + "," + "External" + "\n")

# loop
while True:
	dataFile_sensor = open(outputfile, 'a')
	dataFile_sensor.write(str(time.strftime('%x')) + "," +str(time.strftime('%X') + ","+str(temp1) + "," + str(temp2) + "," + "\n"))
	print "internal temperature = %.0f Celsius" % (temp1)
	print "external temperature = %.0f Celsius" % (temp2)
	time.sleep(30) 























        
