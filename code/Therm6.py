import os
import glob
import time
import subprocess
import datetime

dataFile_sensor = open('/home/thijs/HAB/code/results/temperature.csv', 'a')
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

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
	lines_1 = out_decode.split('\n')
	return lines_1

def read_temp_raw_sensor2():
	catdata = subprocess.Popen(['cat',device_file_sensor2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err = catdata.communicate()
	out_decode = out.decode('utf-8')
	lines_2 = out_decode.split('\n')
	return lines_2

def read_temp_sensor():
        dataFile_sensor = open('/home/thijs/HAB/code/results/temperature.csv', 'a')
        lines_1 = read_temp_raw_sensor1()
        lines_2 = read_temp_raw_sensor2()
        while lines_1[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines_1 = read_temp_raw_sensor1()
        while lines_2[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines_2 = read_temp_raw_sensor2()
        equals_pos_1 = lines_1[1].find('t=')
        if equals_pos_1 != -1:
                temp_string = lines_1[1][equals_pos_1+2:]
                temp_c_1 = float(temp_string) / 1000.0
                return temp_c_1
        equals_pos_2 = lines_2[1].find('t=')
        if equals_pos_2 != -1:
                temp_string = lines_2[1][equals_pos_2+2:]
                temp_c_2 = float(temp_string) / 1000.0
                return temp_c_2
        dataFile_sensor.write(str(datetime.datetime.now().time())+ ","+ str(temp_c_1)+","+ str(temp_c_2)+'\n')

while True:
        read_temp_sensor()
        dataFile_sensor.close()
        time.sleep(30)
