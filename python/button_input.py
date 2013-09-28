#!/usr/bin/python

import RPi.GPIO as GPIO

button1 = 4
button2 = 17 
button3 = 27
button4 = 22


def on_button1(channel):
    print 'Button1 pressed'
def on_button2(channel):
    print 'Button2 pressed'
def on_button3(channel):
    print 'Button3 pressed'
def on_button4(channel):
    print 'Button4 pressed'

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button1, GPIO.RISING, callback=on_button1, bouncetime=1000)
GPIO.add_event_detect(button2, GPIO.RISING, callback=on_button2, bouncetime=200)
GPIO.add_event_detect(button3, GPIO.RISING, callback=on_button3, bouncetime=200)
GPIO.add_event_detect(button4, GPIO.RISING, callback=on_button4, bouncetime=200)


