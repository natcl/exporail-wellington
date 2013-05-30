import serial
import time

pin_list = range(5, 70)
s = serial.Serial('/dev/tty.usbmodem621', 115200)
time.sleep(5)

for pin in pin_list:
    s.write(chr(pin)+chr(1))

time.sleep(5)

for pin in pin_list:
    s.write(chr(pin)+chr(0))

time.sleep(2)
s.close()
