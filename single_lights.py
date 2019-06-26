def station():
    #Lights Code
    test.setmode(test.BOARD)
    test.setup(12, test.OUT)
    test.setup(24, test.OUT)
    test.setup(32, test.OUT)
    test.output(12, True) #Red light On
    time.sleep(3)
    test.output(12, False) #Red light Off
    time.sleep(0.5)
    test.output(24, True) #Orange light On
    time.sleep(3)
    test.output(24, False) #Orange light Off
    time.sleep(0.5)
    test.output(32, True) #Green light On
    time.sleep(3)

    greenstart=time.time() #Start time green light goes on

    while True:

        greenstop=time.time() #Regular time stops for green
        green=greenstop-greenstart #Time duration green light is on

        if green>5: #Check whether green duration time exceeds 5 seconds or the closest object distance exceeds 10 cm

            test.output(32, False) #Green light Off
            time.sleep(0.5)
            test.output(24, True) #Orange light On
            time.sleep(1)
            test.output(24, False) #Orange light Off
            time.sleep(0.5)
            test.output(12, True) #Red light On
            test.output(35, False) #Sensor Off
            break
