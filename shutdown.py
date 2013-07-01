import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH) # Turn ready light on


while True:
  print GPIO.input(8)
  if(GPIO.input(8) == 1):
     print("Request from button to shutdown")
     os.system("sudo shutdown -h now")
     GPIO.cleanup()
     break
  time.sleep(1)
