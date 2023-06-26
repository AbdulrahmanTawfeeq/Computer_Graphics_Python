from tkinter import *
import tkinter

window = Tk()
window.geometry("640x360+320+180")

xfirst = 0
yfirst = 0
xlast = 0
ylast = 0
bold = 1
lineType = "line"

font_color = "black"


def circle():
    global lineType
    lineType = "circle"


def yellow():
    global font_color
    font_color = "yellow"


def red():
    global font_color
    font_color = "red"


def blue():
    global font_color
    font_color = "blue"


def pink():
    global font_color
    font_color = "pink"


def getFirst(event, canvas):
    global xfirst, yfirst
    xfirst = event.x
    yfirst = event.y


def paint(event, canvas):
    global xlast, ylast, xfirst, yfirst, font_color, lineType
    print(event.x, event.y)
    xlast = event.x
    ylast = event.y
    if (lineType == "line"):
        canvas.create_line(xfirst, yfirst, xlast, ylast, fill=font_color, width=bold)
    elif (lineType == "circle"):
        canvas.create_oval(xlast - bold, ylast - bold, xlast + bold, ylast + bold, outline=font_color)
    xfirst = xlast
    yfirst = ylast


def delete(event, canvas):
    if (event.char == 'd'):
        canvas.delete(ALL)


def boldPlus():
    global bold
    bold += 1


def boldMy():
    global bold
    bold -= 1


canvas = Canvas(window, width=640, height=360, bg="tomato")
canvas.pack(side=BOTTOM, expand=True)

yellow = tkinter.Button(window, text="Yellow", bg="yellow", fg="black", command=yellow, width=5)
yellow.pack(side=LEFT, expand=True)

red = tkinter.Button(window, text="Red", bg="red", fg="white", command=red, width=5)
red.pack(side=LEFT, expand=True)

blue = tkinter.Button(window, text="blue", bg="blue", fg="white", command=blue, width=5)
blue.pack(side=LEFT, expand=True)

pink = tkinter.Button(window, text="pink", bg="pink", fg="black", command=pink, width=5)
pink.pack(side=LEFT, expand=True)

boldPlus = tkinter.Button(window, text="+", bg="whitesmoke", fg="black", command=boldPlus, width=2)
boldPlus.pack(side=LEFT, expand=True)

boldMy = tkinter.Button(window, text="-", bg="whitesmoke", fg="black", command=boldMy, width=2)
boldMy.pack(side=LEFT, expand=True)

circle = tkinter.Button(window, text="O", bg="orange", fg="black", command=circle, width=2)
circle.pack(side=LEFT, expand=True)

window.bind("<Button-1>", lambda event: getFirst(event, canvas))
window.bind("<B1-Motion>", lambda event: paint(event, canvas))
window.bind("<Key>", lambda event: delete(event, canvas))

mainloop()

# =============================================================================
# window=Tk(baseName="Lecture 11")
# window.geometry("400x400")
#
# def moveOvalMouse(event, canvas, Object):
#     Object.x=event.x
#     Object.y=event.y
#     oval(canvas, Object)
#
# def oval(canvas, Object):
#     canvas.delete(ALL)
#     canvas.create_rectangle(Object.x-Object.r,
#                    Object.y-Object.r,
#                    Object.x+Object.r,
#                    Object.y+Object.r, fill="#FFFFFF", outline="")
#     canvas.create_rectangle((Object.x+20)-Object.r,
#                    (Object.y+20)-Object.r,
#                    (Object.x+20)+Object.r,
#                    (Object.y+20)+Object.r, fill="#DDDDDD", outline="")
#
#
#
# def moveOval(event, canvas, Object):
#     if(event.keysym == "Up"):
#         Object.y-=1
#     elif (event.keysym == "Down"):
#         Object.y+=1
#     elif (event.keysym == "Right"):
#         Object.x+=1
#     elif (event.keysym == "Left"):
#         Object.x-=1
#     oval(canvas, Object)
#
#
#
# def drawOval(event, canvas, Object):
#     Object.x=event.x
#     Object.y=event.y
#     oval(canvas, Object)
#
#
# class struck():pass
# Object=struck()
#
#
# Object.r=30
# Object.x=13
# Object.y=13
#
# canvas=Canvas(window, width=400, height=400, bg="tomato")
# canvas.pack()
#
# oval(canvas, Object)
#
# window.bind("<Button-1>", lambda event: drawOval(event, canvas, Object))
# window.bind("<Key>", lambda event: moveOval(event, canvas, Object))
# window.bind("<B1-Motion>", lambda event: moveOvalMouse(event, canvas, Object))
#
# mainloop()
# =============================================================================
