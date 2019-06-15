import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for i in range(0,3):
    GPIO.output(7,True)
    time.sleep(4)
    GPIO.output(7,False)
    time.sleep(1)


GPIO.cleanup()
