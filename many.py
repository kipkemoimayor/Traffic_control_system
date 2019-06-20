import RPi.GPIO as GPIO
import time
while True:
    GPIO.setmode(GPIO.BOARD)
    TRIG=11
    ECHO=13
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(5,GPIO.IN)
    GPIO.output(TRIG,True)
    time.sleep(0.0001)
    GPIO.output(TRIG,False)
    GPIO.output(3,True)
    time.sleep(0.0001)
    GPIO.output(3,False)


    while GPIO.input(ECHO)==False:
        start=time.time()

    while GPIO.input(ECHO)==True:
        end=time.time()
    sig_time=end-start

    distance=sig_time/0.000058
    dis=round(distance,0)


    while GPIO.input(5)==False:
        start=time.time()

    while GPIO.input(5)==True:
        end=time.time()
    new_sig=end-start
    d1=new_sig/0.000058
    d=round(d1,0)
    print ("d2 is " + str(d)+' cm')
    print ("distance is " + str(dis)+' cm')
