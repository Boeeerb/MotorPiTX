import motorpitx
import time

Count = 0
while Count < 5:
	motorpitx.out1(True)
	time.sleep(1)
	motorpitx.out1(10)
	time.sleep(2)
	motorpitx.out1(False)
	time.sleep(1)
	Count = Count + 1