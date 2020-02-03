import RPi.GPIO as GPIO
import time

FILE = 'mypipe.txt'


def disconnected():
    GPIO.output(Red_LED, False)
    GPIO.output(Blue_LED, False)

def take_picture():
    GPIO.output(Red_LED, True)
    GPIO.output(Blue_LED, True)

def ready():
    GPIO.output(Red_LED, False)
    GPIO.output(Blue_LED, True)

def readFIFO():
    print("Opening FIFO...")
    print("FIFO opened")
    c = 0
    while c != 3:

        with open(FILE,"r") as fd:
            data = fd.read()
        try :
            c = int(data)   
        except :
            c = 0

        if c == 0:
            disconnected()
        elif c == 1:
            ready()
        elif c == 2:
            take_picture()
        if len(data) == 0:
            pass
        print("Read: '{0}'".format(data))
        time.sleep(0.2)
if __name__=="__main__":
    # Initialize LED as OUPUT
    GPIO.setmode(GPIO.BOARD)
    Red_LED = 11 # Assume that pin 17 is LED Red
    Blue_LED = 13 # Assume that pin 27 is LED Blue
    GPIO.setup(Red_LED, GPIO.OUT)
    GPIO.setup(Blue_LED, GPIO.OUT)

    GPIO.output(Red_LED, False)
    GPIO.output(Blue_LED, False)
    readFIFO()
