import os
import glob
import time
import subprocess
import datetime

dataFile_sensor1 = open('/home/thijs/HAB/code/results/inside.csv', 'a') #creating sensor1.csv
dataFile_sensor2 = open('/home/thijs/HAB/code/results/outside.csv', 'a') #creating sensor1.csv
os.system('modprobe w1-gpio') #Initializing the sensors
os.system('modprobe w1-therm') #Initializing the sensors

#Sensor 28-0000052c5567
base_dir_sensor1 = '/sys/bus/w1/devices/'
device_folder_sensor1 = glob.glob(base_dir_sensor1 + '28-0000052c5567')[0]
device_file_sensor1 = device_folder_sensor1 + '/w1_slave'
#Sensor 28-0000052cc99d
base_dir_sensor2 = '/sys/bus/w1/devices/'
device_folder_sensor2 = glob.glob(base_dir_sensor2 + '28-0000052cc99d')[0]
device_file_sensor2 = device_folder_sensor2 + '/w1_slave'


def read_temp_raw_sensor1():
	catdata = subprocess.Popen(['cat',device_file_sensor1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err = catdata.communicate()
	out_decode = out.decode('utf-8')
	lines = out_decode.split('\n')
	return lines

def read_temp_raw_sensor2():
	catdata = subprocess.Popen(['cat',device_file_sensor2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err = catdata.communicate()
	out_decode = out.decode('utf-8')
	lines = out_decode.split('\n')
	return lines

def read_temp_sensor1():
        dataFile_sensor1 = open('/home/thijs/HAB/code/results/inside.csv', 'a')
        lines = read_temp_raw_sensor1()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw_sensor1()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                dataFile_sensor1.write(str(date.datetime.now)+ ","+ str(temp_c())+'\n') #output format in sensor1.csv
                return temp_c

def read_temp_sensor2():
        dataFile_sensor2 = open('/home/thijs/HAB/code/results/outside.csv', 'a')
        lines = read_temp_raw_sensor2()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw_sensor2()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                dataFile_sensor2.write(str(date.datetime.now)+ ","+ str((temp_c))+'\n') #output format in sensor1.csv
                return temp_c

	
while True:
        read_temp_sensor1()
        read_temp_sensor2()
        dataFile_sensor1.close() #closing the file
        dataFile_sensor2.close() #closing the file
        time.sleep(30) #sleep time in seconds