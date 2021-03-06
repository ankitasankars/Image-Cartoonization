# -*- coding: utf-8 -*-
"""Detail Enhancement Filter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ankitasankars/Image-Cartoonization/blob/main/Detail_Enhancement_Filter.ipynb

### Importing libraries
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

image_path = r"/content/Beetle.jpg"

image = cv2.imread(image_path)

plt.imshow(image)

"""### Applying Detail Enhancement Filter"""

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(image_gray)

image_blur = cv2.medianBlur(image_gray, 3)

plt.imshow(image_blur)

image_edge = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

plt.imshow(image_edge)

"""### Detail Enhancement filter

"""

image_color = cv2.detailEnhance(image, sigma_s=5, sigma_r=0.5)

plt.imshow(image_color)

image_cartoon = cv2.bitwise_and(image_color, image_color, mask=image_edge)

plt.imshow(image_cartoon)