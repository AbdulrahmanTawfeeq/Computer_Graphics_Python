# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:57:38 2020

@author:
"""

# Use Pillow Library to convert the image to ICO
from PIL import Image

img = Image.open("C:/Users/ZETTA/Desktop/image2.png")
img.save("C:/Users/ZETTA/Desktop/image3.ico")
