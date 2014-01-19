from i2clibraries import i2c_adxl345 = i2c_adxl345.i2c_adxl345(0)
adxl345.setContinuousMode()
adxl345.setDeclination(9,54)

# To get degrees and minutes into variables
(degrees, minutes) = adxl345.getDeclination()
(degress, minutes) = adxl345.getHeading()

# To get string of degrees and minutes
declination = adxl345.getDeclinationString()
heading = adxl345.getHeadingString()
