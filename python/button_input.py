#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from wellington import wellingtonPlayer

button1 = 4
button2 = 17 
button3 = 27
button4 = 22

counter = 0
sub = ['parcours2a.json','parcours2b.json','parcours2c.json', 'parcours2d.json']

wp = wellingtonPlayer()

def on_button1(channel):
    print 'Button1 pressed'
    wp.play('parcours1.json')

def on_button2(channel):
    global counter
    print 'Button2 pressed'
    print 'Playing ' + sub[counter]
    wp.play(sub[counter])
    counter = counter + 1
    if counter > 3:
        counter = 0

def on_button3(channel):
    print 'Button3 pressed'
    wp.play('parcours3.json')

def on_button4(channel):
    print 'Button4 pressed'
    wp.stop()
    wp.off()

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(button1, GPIO.FALLING, callback=on_button1, bouncetime=1000)
GPIO.add_event_detect(button2, GPIO.FALLING, callback=on_button2, bouncetime=1000)
GPIO.add_event_detect(button3, GPIO.FALLING, callback=on_button3, bouncetime=1000)
GPIO.add_event_detect(button4, GPIO.FALLING, callback=on_button4, bouncetime=1000)

if sys.flags.interactive:
    pass
else:
    try:
        while True:
            pass
    except KeyboardInterrupt:
        wp.stop()
        wp.off()
        print('Quitting')

