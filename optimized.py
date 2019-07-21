import time
import RPi.GPIO as test
count1 = 0
count2 = 0

def lights():
    test.setmode(test.BOARD)
    test.setup(12,test.OUT)
    test.setup(8,test.OUT)
    test.setup(22,test.OUT)
    test.setup(16,test.OUT)

    test.output(12,True)
    test.output(8,True)
    test.output(22,True)
    test.output(16,True)


def station6():


    test.setmode(test.BOARD)
    test.setup(12, test.OUT)
    test.setup(24, test.OUT)
    test.setup(32, test.OUT)
    test.output(12, True)
    time.sleep(3)
    test.output(12, False)
    time.sleep(0.5)
    test.output(24, True)
    time.sleep(3)
    test.output(24, False)
    time.sleep(0.5)
    test.output(32, True)
    time.sleep(3)

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart


        TRIG=35
        ECHO=33
        test.setup(TRIG,test.OUT)
        test.setup(ECHO,test.IN)
        test.output(TRIG,True)
        time.sleep(1)
        test.output(TRIG,False)

        while test.input(ECHO)==False:
            start=time.time()

        while test.input(ECHO)==True:
            end=time.time()
        sig_time=end-start

        distance=sig_time/0.000058
        dis=round(distance,0)


        if green>5 or dis>10:

            test.output(32, False)
            time.sleep(0.5)
            test.output(24, True)
            time.sleep(1)
            test.output(24, False)
            time.sleep(0.5)
            test.output(12, True)
            break

def station3():


    test.setmode(test.BOARD)
    test.setup(8, test.OUT)
    test.setup(26, test.OUT)
    test.setup(10, test.OUT)
    test.output(8, True)
    time.sleep(3)
    test.output(8, False)
    time.sleep(0.5)
    test.output(26, True)
    time.sleep(3)
    test.output(26, False)
    time.sleep(0.5)
    test.output(10, True)
    time.sleep(3)

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart


        TRIG=31
        ECHO=29
        test.setup(TRIG,test.OUT)
        test.setup(ECHO,test.IN)
        test.output(TRIG,True)
        time.sleep(1)
        test.output(TRIG,False)

        while test.input(ECHO)==False:
            start=time.time()

        while test.input(ECHO)==True:
            end=time.time()
        sig_time=end-start

        distance=sig_time/0.000058
        dis=round(distance,0)


        if green>5 or dis>10:

            test.output(10, False)
            time.sleep(0.5)
            test.output(26, True)
            time.sleep(1)
            test.output(26, False)
            time.sleep(0.5)
            test.output(8, True)
            break

def station2and5():

    test.setmode(test.BOARD)
    test.setup(22, test.OUT)
    test.setup(37, test.OUT)
    test.setup(36, test.OUT)
    test.output(22, True)
    time.sleep(3)
    test.output(22, False)
    time.sleep(0.5)
    test.output(37, True)
    time.sleep(3)
    test.output(37, False)
    time.sleep(0.5)
    test.output(36, True)
    time.sleep(3)


    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart


        TRIG=38
        ECHO=23
        test.setup(TRIG,test.OUT)
        test.setup(19,test.OUT)
        test.setup(ECHO,test.IN)
        test.setup(21,test.IN)

        def ne():
            test.output(TRIG,True)
            time.sleep(1)
            test.output(TRIG,False)
            while test.input(ECHO)==False:
                start=time.time()

            while test.input(ECHO)==True:
                end=time.time()

            sig_time=end-start


            distance=sig_time/0.000058
            dis=round(distance,0)
            return dis

        ne()

        def other():
            test.output(19,True)
            time.sleep(1)
            test.output(19,False)
            while test.input(21)==0:
                pass
            start1=time.time()

            while test.input(21)==1:
                pass
            end1=time.time()
            new_sig=end1-start1
            d1=new_sig*17000
            d=round(d1,0)
            return d

        other()

        stat2=ne()
        stat5=other()



        if green>5 or (stat2>15 and stat5>15):

            test.output(36, False)
            time.sleep(0.5)
            test.output(37, True)
            time.sleep(1)
            test.output(37, False)
            time.sleep(0.5)
            test.output(22, True)
            break

def station1and4():


    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    time.sleep(3)


    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart


        TRIG=11
        ECHO=13
        test.setup(TRIG,test.OUT)
        test.setup(3,test.OUT)
        test.setup(ECHO,test.IN)
        test.setup(5,test.IN)

        def ne():
            test.output(TRIG,True)
            time.sleep(1)
            test.output(TRIG,False)
            while test.input(ECHO)==False:
                start=time.time()

            while test.input(ECHO)==True:
                end=time.time()

            sig_time=end-start


            distance=sig_time/0.000058
            dis=round(distance,0)
            return dis

        ne()

        def other():
            test.output(3,True)
            time.sleep(1)
            test.output(3,False)
            while test.input(5)==0:
                pass
            start1=time.time()

            while test.input(5)==1:
                pass
            end1=time.time()
            new_sig=end1-start1
            d1=new_sig*17000
            d=round(d1,0)
            return d

        other()

        stat1=ne()
        stat4=other()



        if green>5 or (stat1>15 and stat4>15):

            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(16, True)
            break

def traffic_system():
    lights()
    while True:
        station1and4()
        station6()
        station2and5()
        station1and4()
        station3()
        station2and5()

traffic_system()
