import time
import RPi.GPIO as test
count1 = 0
count2 = 0

def station6():

    '''
    Code to operate double lane traffic lights on a double lane
    '''

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
        dis6=round(distance,0)


        if green>120 or dis6>10:

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            station5()



def station5():

    '''
    Code to operate single lane to turn left traffic lights on a tripple lane
    '''

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
        dis5=round(distance,0)


        if green>120 or (dis2>10 and dis5>10):

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            count2 += 1

def station4():

    '''
    Code to operate double lane traffic lights on a tripple lane
    '''

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
        dis4=round(distance,0)


        if green>120 or (dis4>10 and dis1>10):

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            count1 += 1
            count2 = 0

def station3():

    '''
    Code to operate double lane traffic lights on a double lane
    '''

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
        dis3=round(distance,0)


        if green>120 or dis>10:

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            station2()

def station2():

    '''
    Code to operate single lane to turn right traffic lights on a tripple lane
    '''

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
        dis2=round(distance,0)


        if green>120 or (dis2>10 and dis5>10):

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            count2 += 1

def station1():

    '''
    Code to operate double lane traffic lights on a tripple lane
    '''

    count1 = 0

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
        dis1=round(distance,0)


        if green>120 or (dis1>10 and dis4>10):

            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            test.output(7, False)
            time.sleep(0.5)
            test.output(7, True)
            break
            count1 += 1


def traffic_system():
    while True:
        station1()
        station4()
        while True:
            if count1==2:
                station6()
                if count2==2:
                    station1()
                    station4()
                    if count1==4():
                        station3()
                        if count2==2:
                            station1()
                            station4()

traffic_system()
