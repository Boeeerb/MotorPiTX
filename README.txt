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

