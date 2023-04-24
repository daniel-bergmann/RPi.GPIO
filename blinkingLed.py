import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

bool = [True, False, True, False, True, False]

for x in bool:
  GPIO.output(18, x)
  time.sleep(.5)
