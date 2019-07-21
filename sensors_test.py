import RPi.GPIO as GPIO
import time

dis=0

while True:
    # Setup triggers and Echos of all sensors
    GPIO.setmode(GPIO.BOARD)
    TRIG=11
    ECHO=13
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(5,GPIO.IN)
    GPIO.setup(35,GPIO.OUT)
    GPIO.setup(31,GPIO.OUT)
    GPIO.setup(33,GPIO.IN)
    GPIO.setup(29,GPIO.IN)
    GPIO.setup(38,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(21,GPIO.IN)


    def station1():
        GPIO.output(TRIG,True)
        time.sleep(1)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==False:
            start=time.time()

        while GPIO.input(ECHO)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station1()
    a=station1()
    print(str(a)+'Station 1 OK')

    def station2():
        GPIO.output(38,True)
        time.sleep(1)
        GPIO.output(38,False)
        while GPIO.input(23)==False:
            start=time.time()

        while GPIO.input(23)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station2()
    b=station2()
    print(str(b)+'Station 2 OK')


    def station4():
        GPIO.output(3,True)
        time.sleep(1)
        GPIO.output(3,False)
        while GPIO.input(5)==0:
            start=time.time()

        while GPIO.input(5)==1:
            end=time.time()

        sig_time=end-start

        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station4()
    d=station4()
    print(str(d)+'Station 4 OK')

    def station3():
        GPIO.output(31,True)
        time.sleep(1)
        GPIO.output(31,False)
        while GPIO.input(29)==False:
            start=time.time()

        while GPIO.input(29)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station3()
    c=station3()
    print(str(c)+'Station 3 OK')

    def station6():
        GPIO.output(35,True)
        time.sleep(1)
        GPIO.output(35,False)
        while GPIO.input(33)==False:
            start=time.time()

        while GPIO.input(33)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station6()
    f=station6()
    print(str(f)+'Station 6 OK')

    def station5():
        GPIO.output(19,True)
        time.sleep(1)
        GPIO.output(19,False)
        while GPIO.input(21)==False:
            start=time.time()

        while GPIO.input(21)==True:
            end=time.time()

        sig_time=end-start


        distance=sig_time/0.000058
        dis=round(distance,0)
        return dis
    station5()
    e=station5()
    print(str(e)+'Station 5 OK')
