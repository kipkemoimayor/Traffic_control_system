import time
import RPi.GPIO as test


def station1():
    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.output(7, True)
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(7, True)
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(7, True)
 
    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
 

        TRIG=11
        ECHO=13
        test.setup(TRIG,test.OUT)
        test.setup(ECHO,test.IN)
        test.output(TRIG,True)
        time.sleep(0.0001)
        test.output(TRIG,False)

        while test.input(ECHO)==False:
            start=time.time()

        while test.input(ECHO)==True:
            end=time.time()
        sig_time=end-start

        distance=sig_time/0.000058
        dis=round(distance,0)


        if green>120 or dis>10:

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            
    
station1()




