import RPi.GPIO as GPIO

import time

def count(timer):
    for i in range(1,timer):
        time.sleep(1)
        timer-=1
        print(timer)
while True:

    GPIO.setmode(GPIO.BOARD)
    TRIG=11
    ECHO=13
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==False:
        start=time.time()

    while GPIO.input(ECHO)==True:
        end=time.time()
    sig_time=end-start

    distance=sig_time/0.000058
    dis=round(distance,0)
    print ("distance is " + str(dis)+' cm')

    if dis<5:
        GPIO.output(16,False)


        GPIO.output(7,True)
        print("Red lights: STOP")
        time.sleep(5)
        GPIO.output(7,False)
        GPIO.output(16,True)
        print("Get ready: READY")
        time.sleep(1)
        GPIO.output(7,True)
        print("Green lights: Go")
        time.sleep(10)
        GPIO.output(7,False)
        print("Get ready to stop")
        count(4)
        GPIO.output(7,False)


    else:
        GPIO.output(7,False)
        for i in range(0,3):
            GPIO.output(16,True)
            time.sleep(0.05)



    GPIO.cleanup()
