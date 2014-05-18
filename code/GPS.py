import gps
import time

dataFile_sensor = open('/home/pi/HAB/code/results/gps.csv', 'a')
dataFile_sensor.write("time"+","+"speed"+","+"longtitude"+","+"climb"+","+"latitute"+","+"altitute"+"\n")

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    dataFile_sensor = open('/home/pi/HAB/code/results/gps.csv', 'a')
    report = session.next()
    if report['class'] == 'TPV':
        if hasattr(report, 'time'):
            gpstime = report.time
            speed = report.speed* gps.MPS_TO_KPH
            lon = report.lon
            lat = report.lat
            alt = report.alt
            epx = report.epx
            epv = report.epv
            epy = report.epy
            climb = report.climb
            device = report.device
while True:
    dataFile_sensor.write(str(gpstime) + "," + str(speed) + "," + str(lon)+"," + str(climb)+ "," + str(lat)+ "," + str(alt)+ "\n"
    time.sleep(5)