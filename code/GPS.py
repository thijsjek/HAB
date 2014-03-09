from gps import *
import time
import threading
import math
dataFile_GPS = open('Opslaglocatie GPS', 'a')

class GpsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.running = False
    
    def run(self):
        self.running = True
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stopController(self):
        self.running = False
  
    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

if __name__ == '__main__':
    # create the controller
    gpsc = GpsController() 
    try:
        # start controller
        gpsc.start()
        while True:
            print "latitude ", gpsc.fix.latitude
            print "longitude ", gpsc.fix.longitude
            print "time utc ", gpsc.utc, " + ", gpsc.fix.time
            print "altitude (m)", gpsc.fix.altitude
            print "eps ", gpsc.fix.eps
            print "epx ", gpsc.fix.epx
            print "epv ", gpsc.fix.epv
            print "ept ", gpsc.gpsd.fix.ept
            print "speed (m/s) ", gpsc.fix.speed
            print "climb ", gpsc.fix.climb
            print "track ", gpsc.fix.track
            print "mode ", gpsc.fix.mode
            print "sats ", gpsc.satellites
            dataFile_GPS.write(gpsc.fix.latitude +"\t"+ gpsc.fix.longitude +"\t"+ gpsc.utc + " + " + gpsc.fix.time +"\t"+ gpsc.fix.altitude +"\t"+ gpsc.fix.eps +"\t"+ gpsc.fix.epv +"\t"+ gpsc.gpsd.fix.ept+"\t"+ gpsc.fix.speed  + gpsc.fix.climb +"\t"+ gpsc.fix.climb +"\t"+ gpsc.fix.track +"\t"+ gpsc.fix.mode +"\t"+ gpsc.satellites +"\t"+'\n')
            dataFile_GPS.close()
     except:
        print "Stopping gps controller"
        gpsc.stopController()
        #wait for the tread to finish
        gpsc.join()
      
    print "Done"
    time.sleep(20)