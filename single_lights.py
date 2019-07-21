RED=0
ORANGE=0
GREEN=0

def station(RED. ORANGE, GREEN):
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

        if green>5: #Check whether green duration time exceeds 5 seconds or the closest object distance exceeds 10 cm

            test.output(GREEN, False) #Green light Off
            time.sleep(0.5)
            test.output(ORANGE, True) #Orange light On
            time.sleep(1)
            test.output(ORANGE, False) #Orange light Off
            time.sleep(0.5)
            test.output(ORANGE, True) #Red light On
            test.output(RED, False) #Sensor Off
            break
