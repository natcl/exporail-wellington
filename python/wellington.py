import serial
import time
import json
import sys

if sys.platform == 'linux2':
    mega1_port = '/dev/ttyACM0'
    mega2_port = '/dev/ttyACM1'
if sys.platform == 'darwin':
    mega1_port = '/dev/tty.usbmodem411'
    mega2_port = '/dev/tty.usbmodem621'

pin_list = range(5, 70)
mega1 = serial.Serial(mega1_port, 115200)
mega2 = serial.Serial(mega2_port, 115200)
time.sleep(5)

'''for pin in pin_list:
    mega1.write(chr(pin)+chr(1))
    mega2.write(chr(pin)+chr(1))

time.sleep(5)

for pin in pin_list:
    mega1.write(chr(pin)+chr(0))
    mega2.write(chr(pin)+chr(0))

time.sleep(5)
mega1.close()
mega2.close()
'''

with open('pin_mapping.json') as f:
    pin_mapping = json.loads(f.read())

with open('parcours1.json') as f:
    parcours1 = json.loads(f.read())


for event in sorted([int(key) for key in parcours1.keys()]):
    print event
    for light in parcours1[str(event)]:
        arduino = pin_mapping[str(light[0])][0]
        pin = pin_mapping[str(light[0])][1]
        state = light[1]
        if arduino == 1:
            mega1.write(chr(pin)+chr(state))
        if arduino == 2:
            mega2.write(chr(pin)+chr(state))

    time.sleep(0.5)

time.sleep(5)

mega1.close()
time.sleep(2)
mega2.close()
