def station(RED, ORANGE, GREEN, TRIG, ECHO, COUNT, AVERAGE):
    #Lights Code
    test.setmode(test.BOARD)
    test.setup(RED, test.OUT)
    test.setup(ORANGE, test.OUT)
    test.setup(GREEN, test.OUT)
    test.output(RED, True) #Red light On
    time.sleep(3)
    test.output(RED, False) #Red light Off
    time.sleep(0.5)
    test.output(ORANGE, True) #Orange light On
    time.sleep(3)
    test.output(ORANGE, False) #Orange light Off
    time.sleep(0.5)
    test.output(GREEN, True) #Green light On
    time.sleep(3)

    greenstart=time.time() #Start time green light goes on

    while True:

        greenstop=time.time() #Regular time stops for green
        green=greenstop-greenstart #Time duration green light is on

        #Sensors code
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
        dis=round(distance,0) #Distance of closest object from sensor


        if green>5 or dis>10: #Check whether green duration time exceeds 5 seconds or the closest object distance exceeds 10 cm

            test.output(GREEN, False) #Green light Off
            time.sleep(0.5)
            test.output(ORANGE, True) #Orange light On
            time.sleep(1)
            test.output(ORANGE, False) #Orange light Off
            time.sleep(0.5)
            test.output(RED, True) #Red light On
            test.output(TRIG, False) #Sensor Off

            AVERAGE += green # Adding the green times and storing the value to average
            COUNT += 1 # Counting number of times green times are added

            # Route description code
            if COUNT == 3:
                AVERAGE = AVERAGE/3 # Finding average of green time
                COUNT = 0 # Reseting counter

                if AVERAGE < 2.5:
                    print('-------------------------------------------------------------------------')
                    print('Road six is currently not busy with an average green time of '+ str(green))
                else:
                    print('-------------------------------------------------------------------------')
                    print('Road six is currently very busy with average green time of '+ str(green))

                AVERAGE = 0 # Reseting average value
            break
