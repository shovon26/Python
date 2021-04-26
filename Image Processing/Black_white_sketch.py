import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('/home/shovon26/Desktop/sp_effect/oil_paint.jpg')
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

plt.subplot(2,2,1)
plt.axis('off')
plt.imshow(img)

plt.subplot(2,2,3)
plt.axis('off')
plt.imshow(dst_gray)

plt.subplot(2,2,2)
plt.axis('off')
plt.imshow(dst_color)
plt.show()
