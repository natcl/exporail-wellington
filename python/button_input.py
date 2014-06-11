#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from wellington import wellingtonPlayer

button1 = 2
button2 = 3
button3 = 4
button4 = 17
button5 = 27
button6 = 22 
button7 = 10
button8 = 9
button9 = 11

wp = wellingtonPlayer()

def on_button1(channel):
    print 'Button1 pressed'
    wp.play('parcours1a.json')

def on_button2(channel):
    print 'Button2 pressed'
    wp.play('parcours1b.json')

def on_button3(channel):
    print 'Button3 pressed'
    wp.play('parcours1c.json')

def on_button4(channel):
    print 'Button4 pressed'
    wp.play('parcours1d.json')

def on_button5(channel):
    print 'Button5 pressed'
    wp.play('parcours1e.json')

def on_button6(channel):
    print 'Button6 pressed'
    wp.play('parcours2.json')

def on_button7(channel):
    print 'Button7 pressed'
    wp.play('parcours3a.json')

def on_button8(channel):
    print 'Button8 pressed'
    wp.play('parcours3b.json')

def on_button9(channel):
    print 'Button9 pressed'
    wp.stop()
    wp.off()

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(button1, GPIO.FALLING, callback=on_button1, bouncetime=1000)
GPIO.add_event_detect(button2, GPIO.FALLING, callback=on_button2, bouncetime=1000)
GPIO.add_event_detect(button3, GPIO.FALLING, callback=on_button3, bouncetime=1000)
GPIO.add_event_detect(button4, GPIO.FALLING, callback=on_button4, bouncetime=1000)
GPIO.add_event_detect(button5, GPIO.FALLING, callback=on_button5, bouncetime=1000)
GPIO.add_event_detect(button6, GPIO.FALLING, callback=on_button6, bouncetime=1000)
GPIO.add_event_detect(button7, GPIO.FALLING, callback=on_button7, bouncetime=1000)
GPIO.add_event_detect(button8, GPIO.FALLING, callback=on_button8, bouncetime=1000)
GPIO.add_event_detect(button9, GPIO.FALLING, callback=on_button9, bouncetime=1000)


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

