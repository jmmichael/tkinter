'''
http://apprize.info/hardware/raspberry/10.html
This defines a class called App that contains most of the application code.
The command option runs the update command every time the value of the slider is changed.
This updates the duty cycle of the output pin.

'''
from Tkinter import *

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

pwm = GPIO.PWM(16, 500)

pwm.start(100)

class App:

    def __init__(self, master):

        frame = Frame(master)

        frame.pack()

        scale = Scale(frame, from_=0, to=100,

              orient=HORIZONTAL, command=self.update)

        scale.grid(row=0)

    def update(self, duty):

        pwm.ChangeDutyCycle(float(duty))

root = Tk()

root.wm_title('PWM Power Control')

app = App(root)

root.geometry("200x50+0+0")

root.mainloop()
