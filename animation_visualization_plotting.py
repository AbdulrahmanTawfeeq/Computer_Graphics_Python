# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:14:45 2020

@author:
"""

# =============================================================================
# from PIL import Image
# jpg=Image.open("C:/Users/ZETTA/Desktop/image2.jpg")
# jpg.save("C:/Users/ZETTA/Desktop/new.ico")
# =============================================================================

# =============================================================================
# from tkinter import *
# import time
# window=Tk(className="My_Animation")
# window.geometry("400x400")
# window.iconbitmap("C:/Users/ZETTA/Desktop/new.ico")
# 
# canvas=Canvas(window,width=300,height=400,bg="tomato")
# ball=canvas.create_oval(10,10,50,50,fill="blue",outline="tomato")
# canvas.pack()
# 
# x=1
# y=3
# while True:
#     canvas.move(ball,x,y)
#     pos=canvas.coords(ball)
#     x+=1
#     y+=1
#     
#     if(pos[2]>=300 or pos[0]<=0):
#         x=-x
#     if(pos[3]>=400 or pos[1]<=0):
#         y=-y
#         
#     window.update()
#     time.sleep(0.1)
# 
# window.mainloop()
# =============================================================================


# =============================================================================
# from vpython import *
# 
# earth=sphere(
#        pos=vector(-5,0,5),
#        texture=textures.earth,
#        size=vector(1,1,1)
#        )
# 
# ring(
#        pos=vector(0,0,5),
#        texture=textures.wood,
#        radius=1
#        )
# 
# 
# print(earth.pos)
# 
# d=0
# while True:
#     rate(1000)
#     earth.pos=vector(d,0,5)
#     d+=1
#     
#     if (earth.pos.x>=5):
#         for i in range(10):
#             rate(1000)
#             d-=1
#             earth.pos=vector(d,0,5)
# =============================================================================

# =============================================================================
# from vpython import *
# ball=sphere(
#     texture=textures.rug,
#     radius=0.5,
#     axis=vector(1,0,0)
#     )
# 
# while True:
#     rate(10)
#     ball.rotate(angle=1,axis=vector(1,0,0))
# =============================================================================


# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# 
# x = np.arange(0, 100, 1)
# 
# plt.plot(x)
# =============================================================================


from vpython import *

ball = sphere(texture=textures.earth)

local_light(pos=vector(1, 1, 1), color=color.red)

while True:
    rate(1)
    ball.rotate(angle=6, axis=vector(1, 0, 0))
