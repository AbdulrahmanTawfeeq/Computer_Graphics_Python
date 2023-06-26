from tkinter import *


def redrawAll(canvas, Object):
    canvas.create_oval(Object.x - Object.r,
                       Object.y - Object.r,
                       Object.x + Object.r,
                       Object.y + Object.r)
    if Object.charText != "":
        canvas.create_text(20, 20,
                           text="char: " + Object.charText)
    if Object.keysymText != "":
        canvas.create_text(90, 90,
                           text="keysym: " + Object.keysymText)


def run(width=300, height=300):
    def mousePressed(event, canvas, Object):
        Object.x = event.x
        Object.y = event.y

        canvas.delete(ALL)
        redrawAll(canvas, Object)

    def keyPressed(event, canvas, Object):
        Object.charText = event.char
        Object.keysymText = event.keysym
        canvas.delete(ALL)
        redrawAll(canvas, Object)

    class Struct(object): pass

    Object = Struct()
    window = Tk()

    Object.r = 30
    Object.x = 20
    Object.y = 20
    Object.charText = ""
    Object.keysymText = ""

    canvas = Canvas(window, width=width, height=height, bg="tomato")
    canvas.pack()

    window.bind("<Button-1>", lambda event: mousePressed(event, canvas, Object))
    window.bind("<Key>", lambda event: keyPressed(event, canvas, Object))

    window.mainloop()


run(400, 500)
