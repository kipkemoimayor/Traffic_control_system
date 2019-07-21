import time
import RPi.GPIO as test

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
            break


def traffic_system():
    lights() # Begin with all lights red
    while True:
        station(16, 7, 40, 11, 13) # Station 1 and 4
        station(12, 24, 32, 35, 33) # Station 6
        station(22, 37, 36, 38, 23) # Station 2 and 5
        station(16, 7, 40, 11, 13) # Station 1 and 4
        station(8, 26, 10, 31, 29) # Station 3
        station(22, 37, 36, 38, 23) # Station 2 and 5

traffic_system()
