#! /bin/sh

make clean
make
make install
scp v4l2grab led.py user@192.168.1.19:/home/user

