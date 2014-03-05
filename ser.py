import serial, time, csv, sys
import pythoncom, pyHook
import msvcrt
import threading
import Tkinter as tk

def handleKeypress(event):
    pressedKey = event.char
    print pressedKey

def OnKeyboardEvent(event):
    print 'Key:', event.Key
    if event.KeyID == 27:
        hm.UnHookKeyboard()
        pythoncom.PostQuitMessage()
    if event.KeyID == 87:
        ser.write('wxs 1\n')
    if event.KeyID == 83:
        ser.write('wxs -1\n')
    if event.KeyID == 65:
        ser.write('wys -1\n')
    if event.KeyID == 68:
        ser.write('wys 1\n')
    if event.KeyID == 81:
        ser.write('wzs 1\n')
    if event.KeyID == 69:
        ser.write('wzs -1\n')
    
# return True to pass the event to other handlers
    return True
 
class ReadThread(threading.Thread):
    def run(self):
        while(True):
            commout()


def commout():
    read_val = ser.read(size=64)
    while read_val is not '':
        print read_val
        read_val = ser.read(size=64)

def execute(comm, ser):
    ser.write(comm)
    commout()

def usrIn():
    x = raw_input('$')
    x = x + '\n'
    return x

def detectKey():
    inp = ord(msvcrt.getch())
    #print(inp)
    
    if (inp != 255):
        print(inp)
        com = usrIn()
    else:
        com = ''
    return com

def keycont():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()
    

ser = serial.Serial('COM2', 57600, timeout=1)
ser.close()
ser.open()
time.sleep(2)
commout()
commthread = ReadThread()
commthread.start()

#mainHandle = tk.Tk()
#mainHandle.bind_all('<Key>', handleKeypress)
#mainHandle.withdraw()
#mainHandle.mainloop()

print 'END----!!'
#x = detectKey()

x = raw_input('$')
x = x + '\n'
while 1:
    if x == 'rd':
        commout()
    else:
        ser.write(x)
    
    commout()
    x = raw_input('$')
    if x == 'qnow':
        break
    if x == 'sqnow':
        ser.write('shutdown now\n')
        commout()
        break
    if x == 'kcstart':
        keycont()

    x = raw_input('$')
    x = x + '\n'
    
'''
    x = detectKey()
    commout()
    if x != '':
        execute(comm=x, ser=ser)

    
    #x = detectKey
    print(detectKey())
    #x = raw_input('$')
    #x = x + '\n'
    ser.write('ready \n')
    '''
    
print 'a'
ser.close()
