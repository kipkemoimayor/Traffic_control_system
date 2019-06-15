import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
TRIG=11
ECHO=13
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,True)
time.sleep(0.0001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==False:
    start=time.time()

while GPIO.input(ECHO)==True:
    end=time.time()
sig_time=end-start

distance=sig_time/0.000058
print (f"distance is {distance} cm")

GPIO.cleanup()
