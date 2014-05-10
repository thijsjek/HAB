import gps
import time
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
	try:
                dataFile_sensor = open('/home/pi/HAB/code/results/gps.csv', 'a')
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
		if report['class'] == 'TPV':
		    if hasattr(report, 'time'):
                        time = report.time
                        speed = report.speed* gps.MPS_TO_KPH
                        lon = report.lon
                        lat = report.lat
                        alt = report.alt
                        epx = report.epx
                        epv = report.epv
                        epy = report.epy
                        climb = report.climb
                        device = report.device
                        dataFile_sensor.write(str(time), + str(speed), + str(lon))
                        dataFile_sensor.close()
                      
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print "GPSD has terminated"