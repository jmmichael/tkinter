'''
http://apprize.info/hardware/raspberry/10.html
This defines a class called App that contains most of the application code.
Its initializer function creates a member variable called check_var that contains an
instance of BooleanVar that is then supplied as the variable option to the checkbutton.
This ensures that every time the checkbutton is clicked, the value in this variable will be changed.
The command option runs the update command every time such a change occurs.

The update function writes the value in check_var to the GPIO output.
'''
from Tkinter import *

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

class App:

    def __init__(self, master):

        frame = Frame(master)

        frame.pack()

        self.check_var = BooleanVar()

        check = Checkbutton(frame, text='Pin 16',

                 command=self.update,

                 variable=self.check_var, onvalue=True, offvalue=False)

        check.grid(row=1)

    def update(self):

        GPIO.output(16, self.check_var.get())

root = Tk()

root.wm_title('On / Off Switch')

app = App(root)

root.geometry("200x50+50+50")

root.mainloop()
