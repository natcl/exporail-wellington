import serial
import time
import json
import sys

if sys.platform == 'linux2':
    mega1_port = '/dev/ttyACM0'
    mega2_port = '/dev/ttyACM1'
if sys.platform == 'darwin':
    mega1_port = '/dev/tty.usbmodem1421'
    mega2_port = '/dev/tty.usbmodem1411'

mega1 = serial.Serial(mega1_port, 115200)
mega2 = serial.Serial(mega2_port, 115200)
time.sleep(5)

with open('pin_mapping.json') as f:
    pin_mapping = json.loads(f.read())

def off():
    mega1.write(chr(255)+chr(3))
    mega2.write(chr(255)+chr(3))

def close():
    off()
    time.sleep(5)

    mega1.close()
    time.sleep(2)
    mega2.close()

def event(filename, event_number):
    with open(filename) as f:
        parcours = json.loads(f.read())
    for light in parcours1[str(event_number)]:
        arduino = pin_mapping[str(light[0])][0]
        pin = pin_mapping[str(light[0])][1]
        state = light[1]
        if arduino == 1:
            mega1.write(chr(pin)+chr(state))
        if arduino == 2:
            mega2.write(chr(pin)+chr(state))

def light(light_number):
    off()
    arduino = pin_mapping[str(light_number)][0]
    pin = pin_mapping[str(light_number)][1]
    if arduino == 1:
        mega1.write(chr(pin)+chr(1))
    if arduino == 2:
        mega2.write(chr(pin)+chr(1))

def play(filename, speed = 1):
    with open(filename) as f:
        parcours = json.loads(f.read())
    
    for event in sorted([int(key) for key in parcours.keys()]):
        print event
        for light in parcours[str(event)]:
            arduino = pin_mapping[str(light[0])][0]
            pin = pin_mapping[str(light[0])][1]
            state = light[1]
            if arduino == 1:
                mega1.write(chr(pin)+chr(state))
            if arduino == 2:
                mega2.write(chr(pin)+chr(state))
        time.sleep(speed)

if len(sys.argv) > 1:
    play(sys.argv[1])

    close()

