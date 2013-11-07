import motorpitx
import time

Count = 0
while Count < 2:
	motorpitx.motor1(0)
	time.sleep(1)
	motorpitx.motor1(-50)
	motorpitx.motor2(40)
	time.sleep(1)
	motorpitx.motor1(50)
	time.sleep(1)
	motorpitx.motor1(100)
	motorpitx.motor2(-50)
	time.sleep(1)
	motorpitx.motor1(-80)
	time.sleep(1)
	Count = Count + 1
