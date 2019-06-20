import RPi.GPIO as GPIO
import time

dis=0
d=0
while True:
    GPIO.setmode(GPIO.BOARD)
    TRIG=11
    ECHO=13
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(5,GPIO.IN)


    def ne():
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==False:
            start=time.time()

        while GPIO.input(ECHO)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    ne()
    def other():
        GPIO.output(3,True)
        time.sleep(0.00001)
        GPIO.output(3,False)
        while GPIO.input(5)==0:
            pass
        start1=time.time()

        while GPIO.input(5)==1:
            pass
        end1=time.time()
        new_sig=end1-start1
        d1=new_sig*17000
        d=round(d1,0)

        return d
    other()


    a=ne()
    print(a)
