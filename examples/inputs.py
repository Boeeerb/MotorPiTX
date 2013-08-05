import motorpitx
import time

Count = 0
while Count < 5:
	print "Input 1: " + str(motorpitx.in1())
	print "Input 2: " + str(motorpitx.in2())
	time.sleep(1)
	Count = Count + 1