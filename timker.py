import serial, time, csv, sys
import pythoncom, pyHook
import msvcrt
import threading
import Tkinter as tk


class ReadThread(threading.Thread):
    def run(self):
        while(True):
            commout()


def commout():
    read_val = ser.read(size=64)
    while read_val is not '':
        print read_val
        read_val = ser.read(size=64)


ser = serial.Serial('COM2', 57600, timeout=1)
ser.close()
ser.open()
time.sleep(2)
commout()
commthread = ReadThread()
commthread.start()

print 'END----!!'

x = raw_input('$')
x = x + '\n'
y = 1
ser.write(str(y)+"\n")
while 1:
    y = y + 1
    print("asdf {}".format(y))
    #ser.write(str(y)+"\n")
    time.sleep(0.1)
    
print 'a'
ser.close()
