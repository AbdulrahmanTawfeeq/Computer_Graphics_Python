# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:42:39 2020

@author: Ahmad
"""

from tkinter import *
import tkinter
import time

window = Tk()
window.geometry("400x400")

firstx = 0
firsty = 0


def firtsXY(event, canvas):
    global firstx
    global firsty
    firstx = event.x
    firsty = event.y


def addLine(event, canvas):
    global firstx
    global firsty
    canvas.create_line(firstx, firsty,
                       event.x, event.y, fill="yellow", width=11)
    firstx = event.x
    firsty = event.y


def delete(event, canvas):
    canvas.delete(ALL)


canvas = Canvas(window, width=400, height=400, bg="tomato")
canvas.pack()
window.bind("<Button-1>", lambda event: firtsXY(event, canvas))
window.bind("<B1-Motion>", lambda event: addLine(event, canvas))
window.bind("<x>", lambda event: delete(event, canvas))

file = open("line.txt", 'r')
value = file.readline()
x1 = value.split()[0]
y1 = value.split()[1]
i = 0
while (i < 431):
    value = file.readline()

    x2 = value.split()[0]
    y2 = value.split()[1]
    canvas.create_line(x1, y1, x2, y2, fill="yellow", width=9)
    x1 = x2
    y1 = y2
    i += 1
    window.update()
    time.sleep(0.01)

mainloop()
