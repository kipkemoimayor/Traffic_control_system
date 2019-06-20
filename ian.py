import time
import RPi.GPIO as test


def station1():
    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.output(7, True)
    print("red")
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(7, True)
    print('orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print("GREEN:"+ str(green))

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
        print ("distance is " + str(dis)+' cm')

        if green>120 or dis>10:
            print('Green')
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            print('orange')
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            print("red")
            test.output(7, True)
            break
            
    
station1()




