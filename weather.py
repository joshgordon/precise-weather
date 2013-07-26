#!/usr/bin/python
# coding=utf8
import os
import platform
import random
print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
<head>  <meta charset="utf-8">
  <title>Most Precise Weather</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
<body class="python">
<h1>Weather Conditions. Very Precise<a href="https://en.wikipedia.org/wiki/Accuracy_and_precision">*</a></h1>"""
temp = str(random.randint(15, 35) + random.random()) + str(random.randint(100000000000000000000000000000000000000,100000000000000000000000000000000000000000))
tempF = str(9.0/5.0 * float(temp) + 32) + str(random.randint(100000000000000000000000000000000000000,100000000000000000000000000000000000000000))

wind = str(random.randint(0, 50) + random.random()) + str(random.randint(10000000000000000000000000000000000000000,100000000000000000000000000000000000000001))
windmph = str(float(wind) * 2.23694) + str(random.randint(100000000000000000000000000000000000000,100000000000000000000000000000000000000000))

rh = str(random.randint(0, 99) + random.random()) + str(random.randint(10000000000000000000000000000000000000,100000000000000000000000000000000000000000))

values = {"clear", "rain", "wind", "hail", "sleet", "showers", "hurricane", "tornado", "apocalypse"} 

conditionArray = random.sample(values, 2)
condition = conditionArray[0] + " with a chance of " + conditionArray[1] + "." 

direction = {"N", "S", "W", "E", "NE", "NW", "SE", "SW", "UP", "DOWN", "SLANTWAYS", "IN YOUR FACE"}



print "Current Temperature: " + temp + " ºC (" + str(tempF) + " ºF)" + "<br>"
print "Current Wind velocity: " + wind + " m/s (" + str(windmph) + " mph) " + str(random.sample(direction, 1)[0]) + "<br>"
print "Current Relative Humidity: " + rh + "% <br>"
print condition



print """\
<br><br>
Inspired by the less precise <a href="http://preciseweather.net">Precise Weather</a><br>
Fork my <del>hideously ugly</del> code that was hacked together in 20 minutes on <a href="http://github.com/joshgordon/precise-weather/">Github</a><br>
<a href="http://joshgordon.net">Main Site</a>

</body>
</html>
"""
