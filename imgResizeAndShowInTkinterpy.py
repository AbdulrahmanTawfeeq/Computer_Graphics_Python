# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:44:18 2020

@author:
"""
import cv2
import numpy as np
from tkinter import *
from tkinter.ttk import *
from PIL import Image
import PIL

window = Tk()

window.title("Image Processing")
# icons = PhotoImage(file='')
# window.iconphoto(False, icons)
lable_for_input = Label(window, text="Image path: ")
lable_for_input.grid(row=0, column=0)

inputField = Entry(window, width=30)
inputField.grid(row=0, column=1)

canWidth = 100
canHight = 100

my_canvas = Canvas(window, width=canWidth, height=canHight)
my_canvas.grid(row=1, column=1)


# C:\Users\ZETTA\Desktop\image.png

def submit():
    my_canvas.delete(ALL)
    my_image = PhotoImage(file=inputField.get())
    if (my_image.width() <= canWidth and my_image.height() <= canHight):
        my_canvas.create_image((canWidth / 2) - (my_image.width() / 2), (canHight / 2) - (my_image.height() / 2),
                               anchor=NW, image=my_image)
        window.mainloop()
    elif (my_image.width() >= canWidth and my_image.height() <= canHight):
        img = Image.open(inputField.get())
        imgRe = img.resize((canWidth, my_image.height() - (my_image.width() - canWidth)), Image.ANTIALIAS)
        imgRe.save("C:/Users/ZETTA/Desktop/image2.png", "png")
        my_imageNew = PhotoImage(file='C:/Users/ZETTA/Desktop/image2.png')
        my_canvas.create_image(0, 0, anchor=NW, image=my_imageNew)
        my_canvas.update()
        window.mainloop()
    elif (my_image.width() <= canWidth and my_image.height() >= canHight):
        img = Image.open(inputField.get())
        imgRe = img.resize((my_image.width() - (my_image.height() - canHight), canHight), Image.ANTIALIAS)
        imgRe.save("C:/Users/ZETTA/Desktop/image2.png", "png")
        my_imageNew = PhotoImage(file='C:/Users/ZETTA/Desktop/image2.png')
        my_canvas.create_image(0, 0, anchor=NW, image=my_imageNew)
        my_canvas.update()
        window.mainloop()
    elif (my_image.width() >= canWidth and my_image.height() >= canHight):
        img = Image.open(inputField.get())
        imgRe = img.resize(
            (my_image.width() - (my_image.width() - canWidth), my_image.height() - (my_image.height() - canHight)),
            Image.ANTIALIAS)
        imgRe.save("C:/Users/ZETTA/Desktop/image2.png", "png")
        my_imageNew = PhotoImage(file='C:/Users/ZETTA/Desktop/image2.png')
        my_canvas.create_image(0, 0, anchor=NW, image=my_imageNew)
        window.mainloop()


def submit2():
    my_canvas.delete(ALL)
    window.mainloop()


button_submit = Button(window, text="Submit", width=10, command=submit)
button_submit.grid(row=0, column=2)

button_submit2 = Button(window, text="Submit2", width=10, command=submit2)
button_submit2.grid(row=0, column=0)

mainloop()
