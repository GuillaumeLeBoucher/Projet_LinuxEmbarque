import RPi.GPIO as GPIO
import time

def disconnected():
    GPIO.output(Red_LED, False)
    GPIO.output(Green_LED, False)

def take_picture():
    GPIO.output(Red_LED, False)
    GPIO.output(Green_LED, True)

def ready():
    GPIO.output(Red_LED, False)
    GPIO.output(Green_LED, True)

def read(pipe):

    with open(pipe) as fifo:
        while(True):
            data = fifo.read()
            c = int(data)

            if c == 0:
                disconnected()
            elif c == 1:
                ready()
            elif c == 2:
                take_picture()

if __name__ == '__main__':
    # Pipe:
    pipe = 'order'

    try:
        os.mkfifo(FIFO, 0666)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    # Initialize LED as OUPUT
    GPIO.setmode(GPIO.BOARD)
    Red_LED = 17 # Assume that pin 17 is LED Red
    Green_LED = 27 # Assume that pin 27 is LED Green
    GPIO.setup(Red_LED, GPIO.OUT)
    GPIO.setup(Green_LED, GPIO.OUT)

    GPIO.output(Red_LED, False)
    GPIO.output(Green_LED, False)

    ready()

    read()

    # Clean LED
    GPIO.cleanup()
