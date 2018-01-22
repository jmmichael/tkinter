'''
http://apprize.info/hardware/raspberry/10.html

Not tested

Similar in operation to the control for a single PWM channel. It needs 3 PWM channels and 3 sliders.
The type of RGB LED used here is a common cathode. If you have the common anode type, then you can still use it,
but connect the common anode to the 3.3V pin on the GPIO connector. You will then find that the slider becomes reversed,
so a setting of 100 becomes off and 0 becomes full on.

LEDs labeled diffused are best because they allow the colours to be mixed better.

'''

from Tkinter import *

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)

GPIO.setup(24, GPIO.OUT)

pwmRed = GPIO.PWM(18, 500)

pwmRed.start(100)

pwmGreen = GPIO.PWM(23, 500)

pwmGreen.start(100)

pwmBlue = GPIO.PWM(24, 500)

pwmBlue.start(100)

class App:

    def __init__(self, master):

        frame = Frame(master)

        frame.pack()

        Label(frame, text='Red').grid(row=0, column=0)

        Label(frame, text='Green').grid(row=1, column=0)

        Label(frame, text='Blue').grid(row=2, column=0)

        scaleRed = Scale(frame, from_=0, to=100,

              orient=HORIZONTAL, command=self.updateRed)

        scaleRed.grid(row=0, column=1)

        scaleGreen = Scale(frame, from_=0, to=100,

              orient=HORIZONTAL, command=self.updateGreen)

        scaleGreen.grid(row=1, column=1)

        scaleBlue = Scale(frame, from_=0, to=100,

              orient=HORIZONTAL, command=self.updateBlue)

        scaleBlue.grid(row=2, column=1)

    def updateRed(self, duty):

        pwmRed.ChangeDutyCycle(float(duty))

    def updateGreen(self, duty):

        pwmGreen.ChangeDutyCycle(float(duty))

    def updateBlue(self, duty):

        pwmBlue.ChangeDutyCycle(float(duty))

root = Tk()

root.wm_title('RGB LED Control')

app = App(root)

root.geometry("200x150+0+0")

root.mainloop()
