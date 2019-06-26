import RPi.GPIO as GPIO
import time

# Set counter to limit running time
def count(timer):
    for i in range(1,timer):
        time.sleep(1)
        timer-=1
        print(timer)


while True:
    # Setup trigger and echo
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
    dis=round(distance,0) # Distance between sensor and closest object

    GPIO.cleanup()
