import motorpitx
import time

Count = 0
while Count < 2:
	motorpitx.servo1(35)
	motorpitx.servo2(10)
	time.sleep(1)
	motorpitx.servo1(120)
	motorpitx.servo2(120)
	time.sleep(2)
	motorpitx.servo1(160)
	motorpitx.servo2(175)
	time.sleep(1)
	Count = Count + 1