import cv2
import numpy
import matplotlib.pyplot as plt
 
img = cv2.imread('/home/shovon26/Desktop/sp_effect/oil_paint.jpg')
 
res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
 
plt.subplot(2,2,1)
plt.axis('off')
plt.imshow(img)

plt.subplot(2,2,2)
plt.axis('off')
plt.imshow(res)
plt.show()
