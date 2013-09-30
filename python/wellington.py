import serial
import time
import json
import sys
import threading

class wellingtonPlayer(threading.Thread):
    def __init__(self):

        if sys.platform == 'linux2':
            mega1_port = '/dev/ttyACM0'
            mega2_port = '/dev/ttyACM1'
        if sys.platform == 'darwin':
            mega1_port = '/dev/tty.usbmodem1421'
            mega2_port = '/dev/tty.usbmodem1411'
        self.playing = False
        self._stop = False
        
        try:
            self.mega1 = serial.Serial(mega1_port, 115200)
            self.mega2 = serial.Serial(mega2_port, 115200)
        except serial.serialutil.SerialException:
            print "Serial device does not exist, writing to file instead."
            self.mega1 = open('mega1.txt', 'w')
            self.mega2 = open('mega2.txt', 'w')

        time.sleep(5)

        with open('pin_mapping.json') as f:
            self.pin_mapping = json.loads(f.read())

    def off(self):
        self.mega1.write(chr(255)+chr(3))
        self.mega2.write(chr(255)+chr(3))

    def close(self):
        self.off()
        time.sleep(5)

        self.mega1.close()
        time.sleep(2)
        self.mega2.close()

    def play_event(self, filename, event_number):
        with open(filename) as f:
            parcours = json.loads(f.read())
        self.event(parcours, event_number)


    def event(self, parcours, event_number):
        for light in parcours[str(event_number)]:
            arduino = self.pin_mapping[str(light[0])][0]
            pin = self.pin_mapping[str(light[0])][1]
            state = light[1]
            if arduino == 1:
                self.mega1.write(chr(pin)+chr(state))
            if arduino == 2:
                self.mega2.write(chr(pin)+chr(state))
            if light[1] == 0:
                print('\tLight {0} off'.format(light[0]))
            if light[1] == 1:
                print('\tLight {0} on'.format(light[0]))
            if light[1] == 2:
                print('\tLight {0} blink'.format(light[0]))
            if light[1] == 3:
                print('All off')


    def light(self, light_number):
        self.off()
        arduino = self.pin_mapping[str(light_number)][0]
        pin = self.pin_mapping[str(light_number)][1]
        if arduino == 1:
            self.mega1.write(chr(pin)+chr(1))
        if arduino == 2:
            self.mega2.write(chr(pin)+chr(1))

    def start(self, filename, speed = 1):
        if not self.playing:
            self.playing = True
            with open(filename) as f:
                parcours = json.loads(f.read())
        
            for event in sorted([int(key) for key in parcours.keys()]):
                print('Event {0}'.format(event))
                self.event(parcours, event)
                time.sleep(speed)
                if self._stop:
                    break;
            self.playing = False
            self._stop = False
            print 'Exited thread'

    def stop(self):
        if self.playing:
            self._stop = True

