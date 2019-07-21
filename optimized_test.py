import time
import RPi.GPIO as test
count14 = 0
count25 = 0
count3 = 0
count6 = 0
av14 = 0
av25 = 0
av3 = 0
av6 = 0

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

    global count6, av6

    print('station 6 running')

    test.setmode(test.BOARD)
    test.setup(12, test.OUT)
    test.setup(24, test.OUT)
    test.setup(32, test.OUT)
    test.output(12, True)
    print('Red 6')
    time.sleep(3)
    test.output(12, False)
    time.sleep(0.5)
    test.output(24, True)
    print('Orange 6')
    time.sleep(3)
    test.output(24, False)
    time.sleep(0.5)
    test.output(32, True)
    print('green 6')
    time.sleep(3)

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>5 or dis>10:

            print('Green 6')
            test.output(32, False)
            time.sleep(0.5)
            test.output(24, True)
            time.sleep(1)
            print('Orange 6')
            test.output(24, False)
            time.sleep(0.5)
            print('Red 6')
            test.output(12, True)
            test.output(35, False)

            av6 += green
            count6 += 1

            if count6 > 3:
                av6 = av6/3
                count6 = 0

                if av6 < 2.5:
                    print('-------------------------------------------------------------------------')
                    print('Road six is currently not busy with an average green time of '+ str(green))
                else:
                    print('-------------------------------------------------------------------------')
                    print('Road six is currently very busy with average green time of '+ str(green))

                av6 = 0
            break

def station3():

    global count3, av3

    print('station 3 running')

    test.setmode(test.BOARD)
    test.setup(8, test.OUT)
    test.setup(26, test.OUT)
    test.setup(10, test.OUT)
    test.output(8, True)
    print('Red 3')
    time.sleep(3)
    test.output(8, False)
    time.sleep(0.5)
    test.output(26, True)
    print('Orange 3')
    time.sleep(3)
    test.output(26, False)
    time.sleep(0.5)
    test.output(10, True)
    print('green 3')
    time.sleep(3)

    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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
        print('dis = ' + str(dis))


        if green>5 or dis>10:

            print('Green')
            test.output(10, False)
            time.sleep(0.5)
            test.output(26, True)
            time.sleep(1)
            print('Orange')
            test.output(26, False)
            time.sleep(0.5)
            print('Red')
            test.output(8, True)
            test.output(31,False)

            av3 += green
            count3 += 1

            if count3 > 3:
                av3 = av3/3
                count3 = 0

                if av3 < 2.5:
                    print('-------------------------------------------------------------------------')
                    print('Road three is currently not busy with an average green time of '+ str(green))
                else:
                    print('-------------------------------------------------------------------------')
                    print('Road three is currently very busy with average green time of '+ str(green))

                av3 = 0
            break

def station2and5():

    global count25, av25

    print('station 2 and 5 running')

    test.setmode(test.BOARD)
    test.setup(22, test.OUT)
    test.setup(37, test.OUT)
    test.setup(36, test.OUT)
    test.output(22, True)
    print('Red 2 and Red 5')
    time.sleep(3)
    test.output(22, False)
    time.sleep(0.5)
    test.output(37, True)
    print('Orange 2 and Orange 5')
    time.sleep(3)
    test.output(37, False)
    time.sleep(0.5)
    test.output(36, True)
    print('Green 2 and Green 5')
    time.sleep(3)


    greenstart=time.time()

    while True:

        greenstop=time.time()
        green=greenstop-greenstart
        print('Green:' + str(green))


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

        print ("distance is " + str(stat2)+' cm')
        print ("d2 is " + str(stat5)+' cm')

        if green>5 or (stat2>15 and stat5>15):

            print('Green 2 and Green 5')
            test.output(36, False)
            time.sleep(0.5)
            test.output(37, True)
            time.sleep(1)
            print('Orange 2 and Orange 5')
            test.output(37, False)
            time.sleep(0.5)
            print('Red 2 and Red 5')
            test.output(22, True)
            test.output(38, False)
            test.output(19,False)

            av25 += green
            count25 += 1

            if count25 > 3:
                av25 = av25/3
                count25 = 0

                if av25 < 2.5:
                    print('-------------------------------------------------------------------------')
                    print('Roads Two and Five are currently not busy with an average green time of '+ str(green))
                else:
                    print('-------------------------------------------------------------------------')
                    print('Roads Two and Five are currently very busy with average green time of '+ str(green))

                av25 = 0
            break

def station1and4():

    global count14, av14

    print('station 1 and 4 running')

    test.setmode(test.BOARD)
    test.setup(7, test.OUT)
    test.setup(16, test.OUT)
    test.setup(40, test.OUT)
    test.output(16, True)
    print('Red 1 and Red 4')
    time.sleep(3)
    test.output(16, False)
    time.sleep(0.5)
    test.output(7, True)
    print('Orange 1 and Orange 4')
    time.sleep(3)
    test.output(7, False)
    time.sleep(0.5)
    test.output(40, True)
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

        print ("distance is " + str(stat1)+' cm')
        print ("d2 is " + str(stat4)+' cm')

        if green>5 or (stat1>15 and stat4>15):

            print('Green 1 and Green 4')
            test.output(40, False)
            time.sleep(0.5)
            test.output(7, True)
            time.sleep(1)
            print('Orange 1 and Orange 4')
            test.output(7, False)
            time.sleep(0.5)
            print('Red 1 and Red 4')
            test.output(16, True)
            test.output(11,False)
            test.output(3,False)

            av14 += green
            count14 += 1

            if count14 > 3:
                av14 = av14/3
                count14 = 0

                if av14 < 2.5:
                    print('-------------------------------------------------------------------------')
                    print('Roads One and Four are currently not busy with an average green time of '+ str(green))
                else:
                    print('-------------------------------------------------------------------------')
                    print('Roads One and Four are currently very busy with average green time of '+ str(green))

                av14 = 0
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
