Current version - 0.1

A self install script will be coming soon, but to get started, grab motorpitx.py and servod and put into your favorite location.
First run servod (this is used to control the servos) by typing:
	./servod

Next use the motorpitx Python module by importing motorpitx into your Python script. See examples folder for more info.

Functions within the module are currently:

import motorpitx



	motorpitx.blink()
		Blink the ready light once
	motorpitx.motor1([-100 - 100])
		Anything less than 0 will turn it backwards (depending on wiring), 0 will stop the motor and > 0 will go foward
	motorpitx.motor2([-100 - 100])
		Same as motor 1, but for motor 2
	motorpitx.out1([0-100])
		Currently being tested for stability, but set output 1 (which is 5v output remember!) PWM'd between 0 (off) and 100 (full 5v)
	motorpitx.out2([0-100])
		Same as out 1, but for out 2
	motorpitx.in1([True/False])
		Returns True if input is +3v3 and False if it is 0v, so a button press is True, release is False
	motorpitx.in2([True/False])
		Same as in 1, but for in 2
	motorpitx.servo1([0-180])
		Tells the servo to move to that specific angle, not yet compatible with 360 degree servos. Setting the angle to 0 will turn off the servo, depending on the servo
	motorpitx.servo2([0-180])
		You guessed it! Same as servo 1

	motorpitx.cleanup()
		Cleans up the pins that has been used, simply put that at the end of your script, or within Exception captures








Any code clean up, suggestions/improvements/additions are greatly welcome!

Servod is a ServoBlaster daemon by Richard Hirst <richardghirst@gmail.com>
https://github.com/richardghirst/PiBits/tree/master/ServoBlaster






Jason Barnett <jase@boeeerb.co.uk>
Web http://www.boeeerb.co.uk
Twitter @Boeeerb


//// Old readme... /////



A couple of scripts to get your started...

Firstly get the files and place the following:

Shutdown and servo script and :

/etc/init.d
  -  shutdown

/etc
  -  shutdown.py
  -  servod


Then type:

sudo chmod +x /etc/init.d/shutdown
sudo update-rc.d shutdown defaults


This will now start automatically, you will notice the ready LED light up next time you start, and you can now safely shutdown your Pi by pressing the power button quickly. (Make sure you save any work that is currently open first!)

To control the servos, just type:

echo 0=120 > /dev/servoblaster

Making servo 1 turn to 120 degrees, or control servo 2 by typing:

echo 1=80 > /dev/servoblaster

And this will turn servo 2 to 80 degrees

