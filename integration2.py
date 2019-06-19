import time
import RPi.GPIO as test
count1 = 0
count2 = 0

def station6():

    print('station 6 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
            break
            station5()



def station5():

    print('station 5 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
            break
            count2 += 1

def station4():

    print('station 4 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
            break
            count1 += 1
            count2 = 0

def station3():

    print('station 3 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
            break
            station2()

def station2():

    print('station 2 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
            break
            count2 += 1

def station1():

    count1 = 0

    print('station 1 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>120 or dis>10:

            print('Green')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange')
            test.output(7, False)
            time.sleep(0.5)
            print('Red')
            test.output(16, True)
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
