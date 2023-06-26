# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:04:36 2020

@author:
"""

# =============================================================================
import cv2

image1 = cv2.imread("C:/Users/ZETTA/Desktop/image.png")
cv2.imshow("Showing Image", image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
# =============================================================================


# =============================================================================
import cv2
import matplotlib.pyplot as plt

image1 = cv2.imread("C:/Users/ZETTA/Desktop/image.png")
image2 = cv2.imread("C:/Users/ZETTA/Desktop/image.png")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGBA))
plt.title("Image1")

plt.subplot(221)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGBA))
plt.title("Image2")

plt.show()

# =============================================================================


# =============================================================================
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/ZETTA/Desktop/image.png")

INTER_CUBIC = cv2.resize(image, (200, 200), interpolation=cv2.INTER_LINEAR)

rotatedImage = cv2.rotate(INTER_CUBIC, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("rotatedImage", rotatedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(image.shape)
# =============================================================================
