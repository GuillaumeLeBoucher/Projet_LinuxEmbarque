import os
import errno

FIFO = 'mypipe'

try:
    os.mkfifo(FIFO, 0666)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

print("Opening FIFO...")
with open(FIFO) as fifo:
    print("FIFO opened")
    while True:
        data = fifo.read()
        print(data.type)
        if len(data) == 0:
            pass
        else:
            print('Read: "{0}"'.format(data))


    print("Writer closed")
