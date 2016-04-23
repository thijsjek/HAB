import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

folderToSave = "/home/pi/timelapse" 
#os.mkdir(folderToSave)

# Set the initial serial for saved images to 1
fileSerial = 1

# Run a WHILE Loop of infinitely
while True:
    
    d = datetime.now()
    if d.hour:
        
        # Set FileSerialNumber to 000X using four digits
        fileSerialNumber = "%04d" % (fileSerial)
        
        # Capture the CURRENT time (not start time as set above) to insert into each capture image filename
        hour = "%02d" % (d.hour)
        mins = "%02d" % (d.minute)
        
        # Define the common parameters 
        imgWidth = 1280 # Max = 2592 
        imgHeight = 720 # Max = 1944
	rotate = 180 	#0-359 
	
        
        
        # The actual line with all the parameters
        os.system("raspistill -w " + str(imgWidth) + "-rot" + str(rotate) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str(fileSerialNumber) + "_" + str(hour) + str(mins) +  ".jpg -n -sh 40 -awb auto -mm average -t 2000")

        # Increment the fileSerial
        fileSerial += 1
        
        # Wait 60 seconds (1 minute) before next capture
        time.sleep(60)
        
    else:
        
        # Just trapping out the WHILE Statement
        print " ====================================== Doing nothing at this time"
