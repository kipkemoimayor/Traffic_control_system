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
    print('Red 6')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange 6')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
    print('green 6')
    test.output(40,False)

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


        if green>15 or dis>10:

            print('Green 6')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange 6')
            test.output(7, False)
            time.sleep(0.5)
            print('Red 6')
            test.output(16, True)
            break

def station3():

    print('station 3 running')

    test.setmode(test.BOARD)
    test.setup(22, test.OUT)
    test.setup(37, test.OUT)
    test.setup(36, test.OUT)
    test.output(22, True)
    print('Red 3')
    time.sleep(3)
    test.output(22, False)
    time.sleep(0.5)
    test.output(37, True)
    print('Orange 3')
    time.sleep(3)
    test.output(37, False)
    time.sleep(0.5)
    test.output(36, True)
    print('green 3')

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


        TRIG=3
        ECHO=5
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


        if green>15 or dis>10:

            print('Green')
            test.output(36, False)
            time.sleep(0.5)
            test.output(37, True)
            time.sleep(1)
            print('Orange')
            test.output(37, False)
            time.sleep(0.5)
            print('Red')
            test.output(22, True)
            break

def station2and5():

    print('station 2 and 5 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.setup(22, test.OUT)
    test.setup(37, test.OUT)
    test.setup(36, test.OUT)
    test.output(16, True)
    test.output(22, True)
    print('Red 2 and Red 5')
    time.sleep(3)
    test.output(16, False)
    test.output(22, False)
    time.sleep(0.5)
    test.output(7, True)
    test.output(37, True)
    print('Orange 2 and Orange 5')
    time.sleep(3)
    test.output(7, False)
    test.output(37, False)
    time.sleep(0.5)
    test.output(40, True)
    test.output(36, True)
    print('Green 2 and Green 5')
    time.sleep(3)


    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


        TRIG=11
        ECHO=13
        test.setup(TRIG,test.OUT)
        test.setup(3,test.OUT)
        test.setup(ECHO,test.IN)
        test.setup(5,test.IN)

        def ne():
            test.output(TRIG,True)
            time.sleep(0.00001)
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
            time.sleep(0.00001)
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

        stat2=ne()
        stat5=other()

        print ("distance is " + str(stat2)+' cm')
        print ("d2 is " + str(stat5)+' cm')

        if green>15 or (stat2>15 and stat5>15):

            print('Green 2 and Green 5')
            test.output(40, False)
            test.output(36, False)
            time.sleep(0.5)
            test.output(7, True)
            test.output(37, True)
            time.sleep(1)
            print('Orange 2 and Orange 5')
            test.output(7, False)
            test.output(37, False)
            time.sleep(0.5)
            print('Red 2 and Red 5')
            test.output(16, True)
            test.output(22, True)
            break

def station1and4():

    print('station 1 and 4 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.setup(22, test.OUT)
    test.setup(37, test.OUT)
    test.setup(36, test.OUT)
    test.output(16, True)
    test.output(22, True)
    print('Red 1 and Red 4')
    time.sleep(3)
    test.output(16, False)
    test.output(22, False)
    time.sleep(0.5)
    test.output(7, True)
    test.output(37, True)
    print('Orange 1 and Orange 4')
    time.sleep(3)
    test.output(7, False)
    test.output(37, False)
    time.sleep(0.5)
    test.output(40, True)
    test.output(36, True)
    print('Green 1 and Green 4')
    time.sleep(3)


    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


        TRIG=11
        ECHO=13
        test.setup(TRIG,test.OUT)
        test.setup(3,test.OUT)
        test.setup(ECHO,test.IN)
        test.setup(5,test.IN)

        def ne():
            test.output(TRIG,True)
            time.sleep(0.00001)
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
            time.sleep(0.00001)
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

        print ("distance is " + str(stat1)+' cm')
        print ("d2 is " + str(stat4)+' cm')

        if green>15 or (stat1>15 and stat4>15):

            print('Green 1 and Green 4')
            test.output(40, False)
            test.output(36, False)
            time.sleep(0.5)
            test.output(7, True)
            test.output(37, True)
            time.sleep(1)
            print('Orange 1 and Orange 4')
            test.output(7, False)
            test.output(37, False)
            time.sleep(0.5)
            print('Red 1 and Red 4')
            test.output(16, True)
            test.output(22, True)
            break

def traffic_system():
    while True:
        station1and4()
        station6()
        station2and5()
        station1and4()
        station3()
        station2and5()

traffic_system()
